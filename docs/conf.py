# -*- coding: utf-8 -*-
#
# -- General configuration -------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'Sphinx theme for dynamic html presentation style'
copyright = u'2012, Sphinx-users.jp'

version = '0.1.3'

# -- Options for HTML output -----------------------------------

extensions = ['sphinxjp.themes.impressjs', ]

html_theme = 'impressjs'
html_use_index = False
