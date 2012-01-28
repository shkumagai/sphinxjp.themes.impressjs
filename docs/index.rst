.. This is sample documentation file for sphinxjp.themes.impressjs.

======================================================
 Welcome to sphinxjp.themes.impressjs's documentation
======================================================

.. impressjs:: quick-start
   :data-x: 0
   :data-y: 0
   :data-scale: 1
   :class: slide

   Quick Start


.. impressjs:: install
   :data-x: 1000
   :data-y: 0
   :data-scale: 1
   :class: slide

   install:

   .. code-block:: bash

      $ easy_install sphinxjp.themes.impressjs


.. impressjs:: setup
   :data-x: 2000
   :data-y: 0
   :data-scale: 1
   :class: slide

   setup your ``conf.py`` with:

   .. code-block:: python

      extensions = ['sphinxjp.themecore']
      html_style = 'impressjs'


.. impressjs:: bash
   :data-x: 3000
   :data-y: 0
   :data-scale: 1
   :class: slide

   and run:

   .. code-block:: bash

      $ make html

   then you will get HTML output like this!

   Have fun!


.. impressjs:: contents
   :data-x: 3500
   :data-y: 0
   :data-z: -500
   :data-rotate-y: 90
   :data-scale: 1

   Contents:

   .. toctree::
      whatisthis
      howtouse
      todo

.. END
