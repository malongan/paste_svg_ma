# FILE: operator.py

import bpy, tempfile, os, re
from bpy.types import Operator
from mathutils import Vector, Euler

# Use relative imports to get code from other files in this addon
from . import utils
from . import ADDON_ID

class VIEW3D_OT_paste_svg(Operator):
    bl_idname = "view3d.paste_svg"
    bl_label = "Paste SVG"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Access preferences using the ADDON_ID
        prefs = context.preferences.addons[ADDON_ID].preferences
        raw = context.window_manager.clipboard
        svg = utils.clean_svg(raw)

        if not re.search(r'<svg\b', svg, flags=re.I):
            self.report({'ERROR'}, "Clipboard does not contain valid SVG")
            return {'CANCELLED'}

        with tempfile.NamedTemporaryFile(delete=False, suffix=".svg") as tmp:
            tmp.write(svg.encode())
            tmp_path = tmp.name

        try:
            pre_objs = set(bpy.data.objects)
            bpy.ops.import_curve.svg(filepath=tmp_path)
            imported = [o for o in bpy.data.objects if o not in pre_objs]
            if not imported:
                self.report({'WARNING'}, "Nothing imported")
                return {'CANCELLED'}

            unit_scale = utils.UNIT_TO_M[prefs.unit]
            target_w   = prefs.default_width  * unit_scale
            extrude_v  = prefs.default_extrude * unit_scale
            bevel_v    = prefs.default_bevel   * unit_scale

            bpy.ops.object.select_all(action='DESELECT')
            for obj in imported:
                obj.select_set(True)
            context.view_layer.update()

            min_corner = Vector((1e6, 1e6, 1e6))
            max_corner = Vector((-1e6, -1e6, -1e6))
            for obj in imported:
                for v in obj.bound_box:
                    world_v = obj.matrix_world @ Vector(v)
                    min_corner = Vector(min(c, w) for c, w in zip(min_corner, world_v))
                    max_corner = Vector(max(c, w) for c, w in zip(max_corner, world_v))

            size = max_corner - min_corner
            scale = target_w / max(size.x, 1e-9)

            for obj in imported:
                obj.scale = (scale, scale, scale)
                obj.location = -scale * Vector((min_corner.x, min_corner.y, 0))
                if obj.type == 'CURVE':
                    obj.data.extrude     = extrude_v
                    obj.data.bevel_depth = bevel_v if extrude_v else 0.0
                    obj["svg_imported"]  = True

            bpy.ops.object.select_all(action='DESELECT')
            for obj in imported:
                obj.select_set(True)
            context.view_layer.objects.active = imported[0]
            context.view_layer.update()

            min_corner = Vector((1e6, 1e6, 1e6))
            max_corner = Vector((-1e6, -1e6, -1e6))
            for obj in imported:
                for v in obj.bound_box:
                    world_v = obj.matrix_world @ Vector(v)
                    min_corner = Vector(min(c, w) for c, w in zip(min_corner, world_v))
                    max_corner = Vector(max(c, w) for c, w in zip(max_corner, world_v))
            center = (min_corner + max_corner) / 2

            bpy.ops.object.empty_add(type='PLAIN_AXES', location=center)
            empty = context.active_object
            empty.name = "SVG_Group"
            empty.empty_display_size = 0.2
            for obj in imported:
                obj.parent = empty
                obj.matrix_parent_inverse = empty.matrix_world.inverted()

            empty.location = context.scene.cursor.location

            bpy.ops.object.select_all(action='DESELECT')
            for obj in imported:
                obj.select_set(True)
                context.view_layer.objects.active = obj
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                obj.select_set(False)
            context.view_layer.objects.active = empty
            for obj in imported:
                obj.select_set(True)

            bpy.context.view_layer.objects.active = empty
            empty.rotation_euler.rotate(Euler((1.570796, 0, 0)))  # X +90°
            bpy.ops.object.select_all(action='DESELECT')
            for obj in imported:
                obj.select_set(True)
            empty.select_set(True)
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            bpy.data.objects.remove(empty, do_unlink=True)

            for obj in imported:
                obj.select_set(True)

        finally:
            os.remove(tmp_path)

        return {'FINISHED'}