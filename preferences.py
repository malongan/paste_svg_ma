# FILE: preferences.py

import bpy
from bpy.types import AddonPreferences
from bpy.props import FloatProperty, EnumProperty

# Import the addon's ID from the main __init__.py
from . import ADDON_ID

class PasteSVGPreferences(AddonPreferences):
    bl_idname = ADDON_ID

    unit_items = [('m', "m", ""), ('cm', "cm", ""),
                  ('mm', "mm", ""), ('in', "in", ""), ('ft', "ft", "")]
    unit: EnumProperty(name="Unit", items=unit_items, default='m')

    default_width:  FloatProperty(name="Width",  default=2.0,  min=0.000001, precision=6)
    default_extrude: FloatProperty(name="Extrude", default=0.001, min=0.0, precision=6)
    default_bevel:   FloatProperty(name="Bevel",   default=0.0001, min=0.0, precision=6)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "unit")
        layout.prop(self, "default_width")
        layout.prop(self, "default_extrude")
        layout.prop(self, "default_bevel")