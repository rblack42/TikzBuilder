# -*- coding: utf-8 -*-
#
# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import cloud_sptheme as csp

# -- Project information -----------------------------------------------------

project = 'TikzBuilder'
copyright = '2018, Roie R. Black'
author = 'Roie R. Black'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.beta'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.githubpages',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_venv']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------
html_theme = 'cloud'
html_theme_ptah = [csp.get_theme_dir()]
html_theme_options = { "roottarget": "index" }
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'TikzBuilder.tex', 'TikzBuilder',
     'Roie R. Black', 'manual'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_identifier = 'https://github.com/rblack42/TikzBuilder'
epub_uid = 'tb00123'
epub_exclude_files = ['search.html']
