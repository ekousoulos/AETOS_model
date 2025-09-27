# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AETOS_model'
copyright = '2025, Elias Kousoulos-Kovachian, The Cyprus Institute'
author = 'Elias Kousoulos-Kovachian'
release = 'v1.0'

 #-- General configuration -

extensions = [
    "myst_parser","sphinx_design","sphinx_copybutton",          # Allow Markdown files
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

# Theme options to get the wide sidebar + full navigation like RTD
html_theme_options = {
    "collapse_navigation": False,   # keep menu expanded
    "navigation_depth": 4,          # show nested headings
    "titles_only": False,           # include page titles in sidebar
}

# Add logo (place your logo at docs/source/_static/logo.png)
html_logo = "_static/logo.png"

# Custom static files (CSS overrides etc.)
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css",
]

# Syntax highlighting style
pygments_style = "default"          # for light theme
pygments_dark_style = "default"     # for dark theme


myst_enable_extensions = [
    "colon_fence",   # required for sphinx-design blocks
]


# If you want to add custom CSS (optional, e.g., to tweak fonts/spacing)
# Place a custom.css in docs/source/_static/ and uncomment:
# html_css_files = [
#     "custom.css",
# ]