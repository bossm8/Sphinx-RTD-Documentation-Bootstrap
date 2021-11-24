# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '<PROJECT_NAME>'
copyright = '<YEAR>, <PROJECT_NAME>'
author = '<AUTHORS>'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Official supported markdown parser 
    # https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html
    'myst_parser'
]

# Configure file extensions and formats 
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Doc entrypoint
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Default logo configuration
html_logo = '_static/img/logo.svg'
# Default favicon
html_favicon = '_static/img/favicon.svg'

html_theme_options = {
    'logo_only': False,
    'style_external_links': True,
    'display_version': True,
    'navigation_depth': 3,
}

# Some customizations on styles - relative path to _static
html_css_files = []

# Show the link to gitlab on the top right corner
html_context = {
    # Show the gitlab icon and link 
    'display_gitlab': True,
    # Do not show source code in this webpage
    'show_source': False,
    # Text which is shown on the link to gitlab
    'display_text': 'Feature/Bug Report',
    'gitlab_host': '<GITLAB_HOST>',
    'repo_uri': '<REPO_URI>',
    'conf_py_path': '/'
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']