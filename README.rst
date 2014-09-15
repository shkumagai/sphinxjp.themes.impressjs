===========================
 sphinxjp.themes.impressjs
===========================

Impress.js presentation style theme for Sphinx.


Output sample
=============
:output: http://packages.python.org/sphinxjp.themes.impressjs
:source: http://packages.python.org/sphinxjp.themes.impressjs/_sources/index.txt


Feature
=======
* provide ``impressjs`` directive for impress.js presentaion control
* provide ``impressjs`` presentation theme for render HTML document


Installation
============
Make environment with easy_install::

   $ pip sphinxjp.themes.impressjs


setup conf.py with::

   extensions = ['sphinxjp.themes.impressjs']
   html_theme = 'impressjs'
   html_use_index = False


and run::

   $ make html


Requirement
===========
Libraries:

* Python 2.7 or later (not support 3.x)
* Sphinx 1.2.x or later.


Browsers:

* Safari
* Chrome
* Firefox


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.


.. END
