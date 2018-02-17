# IT技術者
# わいわい交流会

嶋田健志 (@TakesxiSximada)

---

## 自己紹介

- Webエンジニア
- Emacs大好き
- Python/Djangoを用いたWeb開発が多い
- もうすぐ12万トゥート@しむどん

---

## 内容

- どのように技術を使い始めたか
- どのように技術を使ってきたか
- スキルアップのために

---

## Pythonとの出会い

+++

### ActivePython

https://www.activestate.com/activepython

+++

#### データフォーマット
#### チェッカー

+++

#### その他書いたもの

- TCP Dummy Server
- 分散しているExcelファイルの集計処理
- GUI操作自動化
- 自動化DSL

などなど...

+++

### Guippy

- GUI操作自動化ライブラリ
- https://pypi.python.org/pypi/guippy
- ユーザー操作をエミュレート
  - キーボード
  - マウス
  - クリップボード

+++

### Guippyの実装

- Win32 APIを呼び出し
- ctypesモジュール
- Pure Python

+++

### Guippyを使って

- 複数のWindowにまたがる操作
- 結果をtextに出力

+++

### 複数のExcelファイル

- いろんなファイルサーバに点在
- 似たようなフォーマットのExcel
- 微細なフォーマットのズレ
- Excelを回収してIronPythonで処理
- Summaryを出す

+++

### IronPython

http://ironpython.net/

Python2.7....

+++

### 今ならもっと違うアプローチもあるかも

---

## スキルアップのために

+++

## 前置き

- 人それぞれのやり方がある
- 無理せず続けるのがよい
- 仕事だけが人生じゃない

+++

## スキルアップをどこでやるか

会社 or 家 or 勉強会 ？

+++

## 誰かとやるのはおすすめ

- ミートアップ
- 勉強会 (スピーチっぽいスタイル)
- もくもく会
- ハンズオン
- ハッカソン


+++

## ミートアップ

- いわゆる交流会
- 情報交換の場
- 刺激を受けにいく感じ
- 作業はしない

+++

## 勉強会

- 話を聞く
- もしくは話す
- まとまった情報が聞けて良い
- 作業はしない

+++

## もくもく会

- 作業がメイン
- テーマに沿った中で自分の作業をする
- 最後にちょっとした発表がある

+++

## ハンズオン

- 作業がメイン
- 教材にそって作業する
- 自由度は少ない
- 講師やTAとして参加もあり
- ただ準備は大変

+++

## ハッカソン

- チームで実際に動くものを作る
- チームは即席で作ることもある
- １日のものもあれば数日のものもある
- 最初から炎上しているプロジェクトっぽさ
- 土日開催ぐらいが参加しやすい
- むっちゃ疲れる


+++

## 大切な一人で素振り

- 興味を持ったトピックに飛びつく
  - トピックはなんでも良い
  - 技術以外のことでもよい
  - モチベーションを保つために
- 途中で諦めてよい
- 好きなときにやめられる自由

+++

## 余談：人生のテーマ

- 好きな時に
- 好きな場所でに
- 好きな人と
- 好きな事を
- 好きなだけ

ちょっとエモすぎ....

+++

## その結果どうなるか

Github Repository 249
https://github.com/TakesxiSximada

殆どがゴミリポジトリ
でもそれでいいと思う

---

## 開発の裏話

+++

2018年1月....

+++

- 毎日夜24時にdiscordで進捗共有
- そのまま繋いで作業
- ふええ

+++

discord便利だ

https://discordapp.com/

+++

- 音声chat
- つなげっぱなし
- リモートワークのチーム運営

---

## 書籍関連

+++

## 今までに関わった書籍

+++

- Pythonエンジニアファーストブック
- Pythonエンジニア養成読本

+++

- 【NEW】初めてのPerl 第7版
- PythonとJavaScriptではじめるデータビジュアライゼーション
- Pythonではじめるデータラングリング
- PythonによるWebスクレイピング

+++

- 開発とは全然違う能力が求められる
- いろんなことを前提にできない
- わかり易い文章、日本語力
- 原書の内容が間違っていることがある

+++

## 例えば...

- 良い: `できます。**
- 悪い: `することができます。**

+++

作業中にアップデートされる言語・ライブラリ

+++

翻訳本の索引と英語

+++

反響があるのがとても嬉しい

---

# いろんな言語を習得には？

+++

いろんな言語、言うほど使えません。

+++

##  Hello World!

これでインストールとか起動とかの方法を覚える

+++

つぎはどうしよう

+++

## デバッグ方法を調べる

- プログラムを書くときにデバッグの方法を知っておくとすごい捗る
- インタラクティブに扱えるのが良い

+++

今回はいくつかの言語のデバッガを調べてみました。

+++

## Pythonのデバッグツール

- pdb
- ipdb
- bpdb
- pudb
- PyCharm

+++

## Pythonのデバッグ


+++

```
def testing():
    import pdb; pdb.set_trace()
    print('one')
    print('two')
    print('three')
    return 1 + 1
```

`import pdb; pdb.set_trace()` この行で停止する

+++

```
testing()
```

+++


## 資料あります

qiita
https://qiita.com/TakesxiSximada/items/45b6d71a44f2706798ed
スライド
https://gitpitch.com/TakesxiSximada/presentations/python-debug-tips#/
動画
https://www.youtube.com/watch?v=w5767tzZwxI

+++

## Emacsのデバッグ

+++

edebug

+++

```init.el
  ;; キーバインド
  (bind-keys :map emacs-lisp-mode-map
             ("C-x C-d" . edebug-defun))

```

+++

```
(defun testing ()
  (message "one")
  (message "two")
  (message "three")
  (+ 1 1))
```

このコードをedebug-defunで評価すると、この関数が呼び出されたときにそこで処理を停止してstep実行できるようになります。


+++

```
(testing) ;; C-x C-e
```

+++

<img src="/images/edebug.png" width="400">


+++




---

# おわり
