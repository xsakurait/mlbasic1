from nntplib import NNTP


時系列データ＝音声、株価や気温
機械学習ではこれらを「数値」に変化することで機械学習処理することができる
強化学習　具体的な入力出力データ（ラベル/教師データ）をやらないが行動ごとに評価が与えられるのでそれを基に判断していく
つまりあり＜なし＜強化の順で自走力が求められる
回帰　中解析分析
　SVM（SVR）SVMは回帰にも分類にも適用できるのでSVRのR(Regression=回帰)で分類している
PLS 部分的最小２条回帰　１００ある変数を１０個にしてから重回帰分析する
NN

分類　SVM(SVC（Classitication）)
決定木
NN　

回帰＝「数値」を予測する

パラメータ　機会に計算してもらいたい値

機械学習の回帰式では　y=w(weight)x+b 数学では傾き＝aを用いる

回帰分析では評価指標は「MSE(平均にじょうごさ)」を用いる

平均二条誤差を小さくするようなパラメータを求めるのは「最小二乗法」　「最尤法（さいゆうほう）」
教師なし学習（分類）のクラスタ数＝グループ数