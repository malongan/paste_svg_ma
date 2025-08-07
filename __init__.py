# FILE: __init__.py

bl_info = {
    "name": "Paste SVG MA",
    "author": "malongan, Refactored by Gemini",
    "version": (3, 0, 0),
    "blender": (3, 0, 0),
    "location": "3D Viewport > N-Panel > Paste SVG MA",
    "description": "One-click paste SVG, auto-bevel, rotate, and unparent. Supports multi-selection parameter synchronization.",
    "category": "Import-Export",
    "doc_url": "https://github.com/your-repo-link-here" # Optional: Add a link to your repo
}

# A constant to hold the addon's ID name (which is the folder name)
# This makes it easy to reference from other files.
ADDON_ID = __name__

# Import all the parts of the addon
from . import preferences
from . import utils
from . import operator
from . import panel

import bpy

# A list of all classes to register
classes = (
    preferences.PasteSVGPreferences,
    operator.VIEW3D_OT_paste_svg,
    panel.VIEW3D_PT_paste_svg,
)

def register():
    """Registers all addon classes."""
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    """Unregisters all addon classes."""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()