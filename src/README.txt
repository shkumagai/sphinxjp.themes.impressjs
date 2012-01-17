Impress.js style presentation theme for Sphinx.

Output Sample
=============
:output: http://packages.python.org/sphinxjp.themes.impressjs
:source: http://packages.python.org/sphinxjp.themes.impressjs/_sources/index.txt


Feature
=======
* provide ``impressjs`` directive for impress.js presentaion control
* provide ``impressjs`` theme for render presentation


Setup
=====
Make environment with easy_install::

    $ easy_install sphinxjp.themes.impressjs


Convert Usage
=============
setup conf.py with::

    extensions = ['sphinxjp.themecore']
    html_theme = 'impressjs'

and run::

    make html


Requirements
============
* Python 2.4 or later (not support 3.x)
* sphinx 1.0.x or later


Presentation Environment
========================
* Chrome
* Firefox
* Safari
* Opera
* Internet Explorer


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific term.
