===========================
 sphinxjp.themes.impressjs
===========================

Impress.js presentation style theme for Sphinx.


Feature
=======
* provide ``impressjs`` directive for impress.js presentaion control
* provide ``impressjs`` presentation theme for render HTML document


Installation
============
Make environment with easy_install::

   $ pip install sphinxjp.themes.impressjs


setup conf.py with::

   extensions = ['sphinxjp.themes.impressjs']
   html_theme = 'impressjs'
   html_use_index = False


and run::

   $ make html


Requirement
===========
Libraries:

* Python 3.9 or later
* Sphinx 7.2 or later.


Browsers:

* Safari
* Chrome
* Firefox


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.


.. END
