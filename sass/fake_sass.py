"""
Run the following command to update the CSS
python fake_sass.py; cp style.css ../qcarchive_sphinx_theme/static/css/style.css
"""

template_files = ["_rtd_overrides.css", "_qca_header.css"]
template = []
for fn in template_files:
    with open(fn, "r") as handle:
        template.append(handle.read()) 
        template.append("/* File {} */".format(fn))

template = "\n".join(template)


colors = {

    # QCA colors
    "qca-light-blue": "#0080C7",
    "qca-dark-blue": "#513D92",
    "qca-black": "#231F20",
    "qca-gray": "#BCBEC0",

    "menu-gray": "#322E2F", # 6% gradient
    "menu-gray2": "#4C4849",
    "menu-gray3": "#656162",
    "white": "white",
    "font-white": "#F5FFFF"
}

associations = {

    # Header
    "HEADER_BACKGROUND_COLOR_LIGHT": "qca-gray",
    "HEADER_BACKGROUND_COLOR": "white",
    "HEADER_FONT_COLOR": "qca-black",
    "HEADER_HOVOR_COLOR": "menu-gray",
    "FONT_HOVOR_COLOR": "font-white",

    # Menu items
    "MENU_BACKGROUND_COLOR": "menu-gray",
    "MENU_BACKGROUND_NESTED_COLOR": "menu-gray2",
    "MENU_BACKGROUND_NESTED_HOVOR_COLOR": "menu-gray3",
    "MENU_BACKGROUND_SEARCH_COLOR": "qca-black",
    "MENU_FONT_HEADER_COLOR": "qca-light-blue",
    "MENU_FONT_COLOR": "font-white", 
}

replacements = {k: colors[v] for k, v in associations.items()}

for k, v in replacements.items():
    template = template.replace(k, v) 


with open("style.css", "w") as handle:
    handle.write(template)
