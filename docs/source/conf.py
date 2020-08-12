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

project = 'Calvin Network Tools'
copyright = '2020, Regents of the University of California'
author = 'Justin Merz, Quinn Hart, Nick Santos'

# The full version, including alpha/beta/rc tags
release = '3.0.7'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_js'
]

primary_domain = 'js'  # mark this as a Javascript project instead of a Python project

# set up the directories to scan for JS files
root_for_relative_js_paths = "../../"
js_source_path = [
    '../../bin',
    '../../bin/cmds',
    '../../bin/cmds/apply-changes-cmds',
    '../../bin/cmds/hec-prm-cmds',
    '../../bin/cmds/hec-prm-cmds/debug-cmds',
    '../../bin/cmds/library-cmds',
    '../../utils/networkInit',
    '../../nodejs',
    '../../nodejs/cmds',
    '../../nodejs/cmds/update-repo',
    '../../nodejs/dss',
    '../../nodejs/excel',
    '../../nodejs/lib',
    '../../nodejs/matrix',
    '../../nodejs/matrix/utils',
    '../../nodejs/pri',
    '../../nodejs/pri/debugger',
    '../../nodejs/pri/format',
    '../../nodejs/shorthand',
    '../../nodejs/update-from-csv',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']