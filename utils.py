# FILE: utils.py

import re

# Unit conversion dictionary
UNIT_TO_M = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'in': 0.0254, 'ft': 0.3048}

def clean_svg(s: str) -> str:
    """Removes unnecessary tags from the SVG string."""
    for pat in (r'<!DOCTYPE[^>]*>', r'', r'</?url[^>]*>', r'<\?xml[^>]*\?>'):
        s = re.sub(pat, '', s, flags=re.I | re.S)
    return s.strip()