.. This is sample documentation file for sphinxjp.themes.impressjs.

======================================================
 Welcome to sphinxjp.themes.impressjs's documentation
======================================================

.. impressjs:: japanese1
   :data-x: 0
   :data-y: 800
   :data-scale: 1

   一枚目のスライド。どれくらいの量のテキス\
   トが書き込めるか、を試してみる。できるだ\
   け多くの文字を含められる方が望ましいが、\
   実際にやってみるとあまり文字が多すぎても\
   読みにくい状態になってしまうだけのような\
   気がしてくるが、この際キニシナイ。感覚的\
   ではあるが、原稿用紙で半分くらいの量なら\
   キレイに収まる程度だろうか。１６０文字。


.. impressjs:: japanese2
   :data-x: 0
   :data-y: 1600
   :data-scale: 1

   欧文の文章ならともかく和文の場合は単語の\
   境界が分かりにくいという難点があるほか、\
   禁則処理などの問題もあるので果たして綺麗\
   に表示できるように記述するにはどのくらい\
   の経験が必要になってくるのだろうか？


.. impressjs:: english1
   :data-x: 1000
   :data-y: 800
   :data-scale: 1

   A first slide. How many words contains each
   slides and it show clearly.


.. impressjs:: diagram1
   :data-x: 2000
   :data-y: 800
   :data-scale: 1

   .. blockdiag::

      diagram {
         A -> B -> C;
              B -> D;
      }


.. impressjs:: diagram2
   :data-x: 2000
   :data-y: 1600
   :data-scale: 1

   .. seqdiag::

      diagram {
         A -> B -> C;
              C -> A;
      }


.. impressjs:: option
   :data-x: 800
   :data-y: 600
   :data-scale: 4

   .. content

.. END
