<link href=".\style.css" rel="stylesheet"></link>

# 画像処理100本ノック
画像処理100本ノック(https://github.com/yoyoyo-yo/Gasyori100knock)をJupyter Notebook上で楽しめるように移植しました．手動なので精度は知りません．多分開くとき激重です．ごめん．
## やったこと
- 全問題全画像を一つのノートで見られるようにした．
- 本家作者の解答コードを埋め込んだ．
- （ちょっと）typoを直した．
## あそびかた
[本家のREADME](https://github.com/yoyoyo-yo/Gasyori100knock/blob/master/README.md)を参考に環境を整えたあと，`画像処理100本ノック(問題編).ipynb`を開くと遊べます．Jupyter Notebookのカーネルを変更しないとコードが実行できないはずなので自分のやり方を以下に示します．Win10です．
1.  `$ conda create --name=gasyori100 python=python3.6 jupyter`  
    でJupyterを含む仮想環境を用意します．
2. `$ conda activate gasyori100`  
    `$ ipython kernel install --user --name=gasyori100 --display-name=gasyori100`  
    で新規Kernelを追加します．
3. うまくいっていれば`画像処理100本ノック(問題編).ipynb`を開いた後の`Kernel`タブに`gasyori100`があるはずなので切り替えます．

ここらへんは環境依存なのでうまく対応してください．<br>
参考: [Jupyterで複数カーネルを簡単に選択するための設定 - Qiita](https://qiita.com/tomochiii/items/8b937f15c79a0c3eae0e)
## TODO
- 問題64の更新を確認する(最終: 02/01)
- 自分で問題を解く(10/100)
<!-- ## AC表
緑色の問題は解答編にコードを載せているので実装の参考にしてください．
<table>
    <th>問題</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8</th>
    <th>9</th>
    <th>10</th>
    <tr>
        <td>01-10</td>
        <td class="ac">1. チャネル入れ替え</td>
        <td class="ac">2. グレースケール化</td>
        <td class="ac">3. 二値化</td>
        <td class="ac">4. 大津の二値化</td>
        <td class="ac">5. HSV変換</td>
        <td class="ac">6. 減色処理</td>
        <td class="ac">7. 平均プーリング</td>
        <td class="ac">8. Maxプーリング</td>
        <td class="ac">9. ガウシアンフィルタ</td>
        <td class="ac">10. メディアンフィルタ</td>
    </tr>
    <tr>
        <td>11-20</td>
        <td>11. 平滑化フィルタ</td>
        <td>12. モーションフィルタ</td>
        <td>13. MAX-MINフィルタ</td>
        <td>14. 微分フィルタ</td>
        <td>15. Sobelフィルタ</td>
        <td>16. Prewittフィルタ</td>
        <td>17. Laplacianフィルタ</td>
        <td>18. Embossフィルタ</td>
        <td>19. LoGフィルタ</td>
        <td>20. ヒストグラム表示</td>
    </tr>
    <tr>
        <td>21-30</td>
        <td>21. ヒストグラム正規化</td>
        <td>22. ヒストグラム操作</td>
        <td>23. ヒストグラム平坦化</td>
        <td>24. ガンマ補正</td>
        <td>25. 最近傍補間</td>
        <td>26. Bi-linear補間</td>
        <td>27. Bi-cubic補間</td>
        <td>28. アフィン変換(平行移動)</td>
        <td>29. アフィン変換(拡大縮小)</td>
        <td>30. アフィン変換(回転)</td>
    </tr>
    <tr>
        <td>31-40</td>
        <td>31. アフィン変換(スキュー)</td>
        <td>32. フーリエ変換</td>
        <td>33. フーリエ変換　ローパスフィルタ</td>
        <td>34. フーリエ変換　ハイパスフィルタ</td>
        <td>35. フーリエ変換　バンドパスフィルタ</td>
        <td>36. JPEG圧縮 (Step.1)離散コサイン変換</td>
        <td>37. PSNR</td>
        <td>38. JPEG圧縮 (Step.2)DCT+量子化</td>
        <td>39. JPEG圧縮 (Step.3)YCbCr表色系</td>
        <td>40. JPEG圧縮 (Step.4)YCbCr+DCT+量子化</td>
    </tr>
    <tr>
        <td>41-50</td>
        <td>41. Cannyエッジ検出 (Step.1) エッジ強度</td>
        <td>42. Cannyエッジ検出 (Step.2) 細線化</td>
        <td>43. Cannyエッジ検出 (Step.3) ヒステリシス閾処理</td>
        <td>44. Hough変換・直線検出 (Step.1) Hough変換</td>
        <td>45. Hough変換・直線検出 (Step.2) NMS</td>
        <td>46. Hough変換・直線検出 (Step.3) Hough逆変換</td>
        <td>47. モルフォロジー処理(膨張)</td>
        <td>48. モルフォロジー処理(収縮)</td>
        <td>49. オープニング処理</td>
        <td>50. クロージング処理</td>
    </tr>
    <tr>
        <td>51-60</td>
        <td>51. モルフォロジー勾配</td>
        <td>52. トップハット変換</td>
        <td>53. ブラックハット変換</td>
        <td>54. テンプレートマッチング SSD</td>
        <td>55. テンプレートマッチング SAD</td>
        <td>56. テンプレートマッチング NCC</td>
        <td>57. テンプレートマッチング ZNCC</td>
        <td>58. ラベリング 4近傍</td>
        <td>59. ラベリング 8近傍</td>
        <td>60. アルファブレンド</td>
    </tr>
    <tr>
        <td>61-70</td>
        <td>61. 4-連結数</td>
        <td>62. 8-連結数</td>
        <td>63. 細線化処理</td>
        <td>64. ヒルディッチの細線化</td>
        <td>65. Zhang-Suenの細線化</td>
        <td>66. HOG (Step.1) 勾配強度・勾配角度</td>
        <td>67. HOG (Step.2) 勾配ヒストグラム</td>
        <td>68. HOG (Step.3) ヒストグラム正規化</td>
        <td>69. HOG (Step.4) 特徴量の描画</td>
        <td>70. カラートラッキング</td>
    </tr>
    <tr>
        <td>71-80</td>
        <td>71. マスキング</td>
        <td>72. マスキング(カラートラッキング＋モルフォロジー)</td>
        <td>73. 縮小と拡大</td>
        <td>74. ピラミッド差分による高周波成分の抽出</td>
        <td>75. ガウシアンピラミッド</td>
        <td>76. 顕著性マップ</td>
        <td>77. ガボールフィルタ</td>
        <td>78. ガボールフィルタの回転</td>
        <td>79. ガボールフィルタによるエッジ抽出</td>
        <td>80. ガボールフィルタによる特徴抽出</td>
    </tr>
    <tr>
        <td>81-90</td>
        <td>81. Hessianのコーナー検出</td>
        <td>82. Harrisのコーナー検出 (Step.1) Sobel + Gauusian</td>
        <td>83. Harrisのコーナー検出 (Step.2) コーナー検出</td>
        <td>84. 簡単な画像認識 (Step.1) 減色化 + ヒストグラム</td>
        <td>85. 簡単な画像認識 (Step.2) クラス判別</td>
        <td>86. 簡単な画像認識 (Step.3) 評価(Accuracy)</td>
        <td>87. 簡単な画像認識 (Step.4) k-NN</td>
        <td>88. K-means (Step.1) 重心作成</td>
        <td>89. K-means (Step.2) クラスタリング</td>
        <td>90. K-means (Step.3) 初期ラベルの変更</td>
    </tr>
    <tr>
        <td>91-100</td>
        <td>91. K-meansによる減色処理 (Step.1) 色の距離によるクラス分類</td>
        <td>92. K-meansによる減色処理 (Step.2) 減色処理</td>
        <td>93. 機械学習の学習データの用意 (Step.1) IoUの計算</td>
        <td>94. 機械学習の学習データの用意 (Step.2) ランダムクラッピング</td>
        <td>95. ニューラルネットワーク (Step.1) ディープラーニングにする</td>
        <td>96. ニューラルネットワーク (Step.2) 学習</td>
        <td>97. 簡単な物体検出 (Step.1) スライディングウィンドウ + HOG</td>
        <td>98. 簡単な物体検出 (Step.2) スライディングウィンドウ + NN</td>
        <td>99. 簡単な物体検出 (Step.3) Non-Maximum Suppressio</td>
        <td>100. 簡単な物体検出 (Step.4) 評価 Precision, Recall, F-score, mAP</td>
    </tr>
<table> -->
