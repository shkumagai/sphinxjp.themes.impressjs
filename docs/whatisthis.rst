Sample slide 1
==============

.. impressjs:: preface
   :data-x: 1000
   :data-y: 1000
   :data-scale: 1

   Python_ 製ドキュメンテーションツール Sphinx_ 専用の
   **HTMLプレゼンテーションテーマ**


.. impressjs:: merit
   :data-x: 2000
   :data-y: 1000
   :data-rotate: 180
   :data-scale: 1

   1. ソースを reStructuredText_ で記述する
   2. HTMLをビルド（\ ``make html``\ を実行）する
   3. プレゼンテーションの出来上がり


.. impressjs:: code-highlight
   :data-x: 3000
   :data-y: 1000
   :data-scale: 1

   ソースコードのハイライトも可能です。

   .. code-block:: python

      def hello(name):
          print "Hello, %s" % name

   .. code-block:: bash

      echo $text | tr "[:upper:]" "[:lower:]"


.. impressjs:: blockdiagram
   :data-x: 1000
   :data-y: 1800
   :data-scale: 1

   blockdiag_ も使えます。

   .. blockdiag::

      diagram {
        A -> B -> C;
             B -> D
      }

.. impressjs:: special-thanks
   :data-x: 2000
   :data-y: 1800
   :data-scale: 1

   このプレゼンテーションは `impress.js`_ を使っています。


.. impressjs:: not-impremented_title
   :data-x: 3000
   :data-y: 1800
   :data-scale: 1

   いまのところできないこと


.. impressjs:: not-implemented_1
   :data-x: 3000
   :data-y: 2000
   :data-z: -200
   :data-scale: 0.3

   - H1,H2...H6 を使えない（意図したレンダリングが出来ない状態）


.. impressjs:: support
   :data-x: 1000
   :data-y: -700
   :data-rotate-y: 90
   :data-scale: 0.5

   推奨ブラウザ

   - Chrome
   - Safari
   - Firefox 10 以降


.. impressjs:: overview
   :data-x: 1500
   :data-y: 900
   :data-scale: 3

   .. overview

.. _Python: http://www.python.org/
.. _Sphinx: http://sphinx.pocco.org
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _impress.js: http://github.com/bartaz/impress.js
.. _blockdiag: http://blockdiag.com/ja/blockdiag/
