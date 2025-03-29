from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath('../../slurmpter'))
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

project = 'slurmpter'
copyright = '2020, Isaac Chun Fung WONG'
author = 'Isaac Chun Fung WONG'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'autodocsumm'
]

autosummary_generate = True

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
html_theme = 'sphinx_rtd_theme'
html_logo = '_static/logo.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def skip_member(app, what, name, obj, skip, opts):
    skipped_slurm_member = ['add_child', 'add_children', 'add_parent', 'add_parents',
                            'add_subdag', 'haschildren', 'hasparents', 'submit_dag']
    if name != '__init__' and name[0] == '_':
        return True
    elif hasattr(obj, '__module__') and obj.__module__=="slurmpter.slurm" and name in skipped_slurm_member:
        return True
    return False

def setup(app):
    app.connect('autodoc-skip-member', skip_member)
