project = 'Open_MICKY'
copyright = '2026, FBOT@Research'
author = 'FBOT@Research'
release = '0.1'

extensions = ["myst_parser"]

source_suffix = {
    ".md": "markdown"
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "table",
]

myst_heading_anchors = 3

html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

html_theme_options = {
    # 🎨 cores
    "light_css_variables": {
        "color-brand-primary": "#2B5D9F",
        "color-brand-content": "#2B5D9F",
    },

    # 🧭 navbar
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],

    # 🔗 ícones (GitHub)
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/fbot-research/open_micky",
            "icon": "fab fa-github",
        },
    ],

    # opcional (recomendado)
    "navbar_align": "left",
    "show_nav_level": 1,
}