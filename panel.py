# FILE: panel.py

import bpy
from bpy.types import Panel

# Use relative imports to get the addon's ID
from . import ADDON_ID

class VIEW3D_PT_paste_svg(Panel):
    bl_label = "Paste SVG"
    bl_idname = "VIEW3D_PT_paste_svg"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SVG导入"  # <<< CHANGED: This creates the new tab in the N-Panel

    def draw(self, context):
        prefs = context.preferences.addons[ADDON_ID].preferences
        layout = self.layout

        layout.operator("view3d.paste_svg", text="Paste SVG", icon="PASTEDOWN")
        col = layout.column(align=True)
        col.label(text=f"Unit: {prefs.unit.upper()}", icon="BLANK1")
        col.prop(prefs, "default_width", text="Width")
        col.prop(prefs, "default_extrude", text="Extrude")
        col.prop(prefs, "default_bevel", text="Bevel")

        sel_curves = [ob for ob in context.selected_objects
                      if ob.type == 'CURVE' and ob.get("svg_imported")]
        if sel_curves:
            layout.separator()
            box = layout.box()
            box.label(text="Object Settings", icon="MODIFIER")
            col = box.column(align=True)
            col.scale_y = 0.9
            col.prop(sel_curves[0].data, "extrude", text="Extrude")
            col.prop(sel_curves[0].data, "bevel_depth", text="Bevel")
            box.operator("object.convert", text="Convert to Mesh").target = 'MESH'