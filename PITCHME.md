# Pepper Python チュートリアル

嶋田健志
(@TakesxiSximada)

---

## 今日のゴール

- [ ] Pepperの開発環境を構築する
- [ ] Pythonの開発環境を構築する
- [ ] Pepperを動かす
- [ ] Pepper + Pythonでプログラムを書いて実行する

---

## Pepperについてざっと説明

- ロボット
- 白い
- 目が大きい

---

## Pythonについてざっと説明

- スクリプト言語
- 最近機械学習のおかげですごい流行っている


---

## Choregrapheのインストール



---

## Choregrapheを起動する

![](images/screen-2017-10-20-16.17.51.png)
![](images/screen-2017-10-20-16.18.03.png)

---

## Choregrapheのライセンス入力画面

- ライセンスキーを持っていればライセンスキーを入力します。
- 今回は `試用期間を継続します。` を選択します。

![](images/screen-2017-10-20-16.18.16.png)


---

## Choregrapheの起動画面

起動するとこのような画面になります。

![](images/screen-2017-10-20-16.32.11.png)


---

## バーチャルロボットの設定

バーチャルロボットを使ってローカル環境でペッパーの操作ができるようにします。

![](images/screen-2017-10-20-16.49.43.png)

---

## ポート番号を確認

- このポート番号につなぐことでPepperを遠隔で操作可能
- pynaoqiでは外部からPepperに接続してPepperを操作する機能が提供されている
- [pynaoqiのインストールガイド](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)

---

## ライブラリへのパスの設定

- ${HOME}/src/var配下にtarballを展開した状態であることを前提としています。
- 必要に応じてパスを書き換えてください。

```
$ export PYTHONPATH=${PYTHONPATH}:${HOME}/src/var/pynaoqi-python2.7-2.5.5.5-mac64/lib/python2.7/site-packages
$ export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:${HOME}/src/var/pynaoqi-python2.7-2.5.5.5-mac64/lib
```

---

## naoqiが使えるかを確認する

naoqiをimportしてImportErrorがでなければOKです。

```
$ python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import naoqi
>>>
```

---

## PepperにHello worldを言わせてみる

- naoqiを使ってPepperを操作する
- バーチャルロボットは音を発生させられない
- 発する音は文字列としてChoregrapheのダイアログに表示される


---

## PythonのInteractiveShellで実行

```
>>> from naoqi import ALProxy
>>> tts = ALProxy("ALTextToSpeech", "127.0.0.1", 54264)
[I] 1508488962.246104 775 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[W] 1508488962.247009 4099 qi.path.sdklayout: No Application was created, trying to deduce paths
[I] 1508488962.247033 775 qimessaging.transportserver: TransportServer will listen on: tcp://10.27.40.30:55925
[I] 1508488962.247048 775 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:55925
[I] 1508488962.247056 775 qimessaging.transportserver: TransportServer will listen on: tcp://192.168.99.1:55925
>>> tts.say("Hello, world!")
>>>
```

@[1](ALProxyをインポート)
@[2](第一引数はALTextToSpeech、第二引数はIPアドレス、第三引数はポート番号)
@[3-7](接続)
@[8](テキスト "Hello world!" をPepperに送信)

---

## ダイアログ

![](images/screen-2017-10-20-17.44.22.png)

ロボットが発話する内容は `ロボット: xxxx` という形で表示されます。

---

## ALTextToSpeech以外を使ってみる

- せっかく色々Pepperを制御できるので色々触ってみましょう。

---

## Pepperを動かす

- Pepperには足元にホイールが付いているので躯体を移動できる
- ホイールの制御には `ALMotion` を使う
- http://doc.aldebaran.com/2-1/naoqi/motion/index.html

---

## 接続

```
>>> motion = ALProxy('ALMotion', '127.0.0.1', 56838)
[I] 1508492002.065112 775 qimessaging.session: Session listener created on tcp:/
/0.0.0.0:0
[I] 1508492002.065938 775 qimessaging.transportserver: TransportServer will list
en on: tcp://10.27.40.30:56852
[I] 1508492002.065968 775 qimessaging.transportserver: TransportServer will list
en on: tcp://127.0.0.1:56852
[I] 1508492002.065981 775 qimessaging.transportserver: TransportServer will list
en on: tcp://192.168.99.1:56852
>>>
```

---

## 前進/後退/停止

### 前進

```
>>> motion.moveToward(0.1,0.0,0.0)
```

### 後退

```
>>> motion.moveToward(-0.1,0.0,0.0)
```

### 停止

```
>>> motion.moveToward(0.0,0.0,0.0)
```

---

## 左右

### 左

```
>>> motion.moveToward(0.0,0.0,0.0)
```

### 右

```
>>> motion.moveToward(0.0,-0.1,0.0)
```

### 停止

```
>>> motion.moveToward(0.0,0.0,0.0)
```

---

## 回転

### 回れ右方向

```
>>> motion.moveToward(0.0,0.0,-0.1)
```

### 回れ左方向

```
>>> motion.moveToward(0.0,0.0,0.1)
```

### 停止

```
>>> motion.moveToward(0.0,0.0,0.0)
```

---

## 障害物を避けながら目的地に移動する

- Pepperは目的地までの経路に障害物があるとそれを避けて動くナビゲーション機能が提供されている
- `ALNavigation` を使う
- http://doc.aldebaran.com/2-1/naoqi/motion/alnavigation-api.html#ALNavigationProxy::navigateTo__floatCR.floatCR


---

## 障害物を避けながら目的地に移動する

```
>>> nav = ALProxy('ALNavigation', '127.0.0.1', 56838)
>>> nav.navigateTo(1, 1)
True
```

`nav.navigateTo(x, y)`

- x: 前後方向をfloatで指定(単位はメートル)。
- y: 左右方向をfloatで指定(単位はメートル)。
- 座標を指定するとまずは躯体を回転させて最短経路で移動
- 移動経路中に障害物があると回避



---

## ポーズをとってみる


```
>>> pos = ALProxy('ALRobotPosture', '127.0.0.1', 56838)
>>> pos.goToPosture('StandZero', 1.0)
True
>>> pos.goToPosture('Stand', 1.0)
True
>>> pos.goToPosture('StandInit', 1.0)
True
```

- 最初は次のポーズしかない
  - StandZero
  - Standinit
  - Stand
  - Crouch
- ポーズは自分でも作成できる
- 存在しないポーズを指定した場合はFalseがreturnされる

![](images/screen-2017-10-20-19.22.28.png)

---

## Pepperの目を光らせる

- ALProxy経由でPepperの目を光らせてみます
- LEDの操作なので `AllLeds` を使う
- http://doc.aldebaran.com/2-1/naoqi/sensors/alleds-api.html?highlight=alled#ALLedsProxy

---

## 接続する

```
>>> leds = ALProxy('ALLeds', '127.0.0.1', 54264)
```


---

## LEDグループ名を取得する

LEDには各パーツごとにLEDがいくつも付いています。それを一つずつ制御するのは大変なのでグループが作成できます。Pepperではすでにグループがいくつも作成されています。そのグループを取得してみましょう。

```
>>> leds.listGroups()
['AllLeds', 'AllLedsBlue', 'AllLedsGreen', 'AllLedsRed', 'ChestLeds', 'EarLed1', 'EarLed10', 'EarLed
2', 'EarLed3', 'EarLed4', 'EarLed5', 'EarLed6', 'EarLed7', 'EarLed8', 'EarLed9', 'EarLeds', 'FaceLed
0', 'FaceLed1', 'FaceLed2', 'FaceLed3', 'FaceLed4', 'FaceLed5', 'FaceLed6', 'FaceLed7', 'FaceLedLeft
0', 'FaceLedLeft1', 'FaceLedLeft2', 'FaceLedLeft3', 'FaceLedLeft4', 'FaceLedLeft5', 'FaceLedLeft6',
'FaceLedLeft7', 'FaceLedRight0', 'FaceLedRight1', 'FaceLedRight2', 'FaceLedRight3', 'FaceLedRight4',
 'FaceLedRight5', 'FaceLedRight6', 'FaceLedRight7', 'FaceLeds', 'FaceLedsBottom', 'FaceLedsExternal'
, 'FaceLedsInternal', 'FaceLedsLeftBottom', 'FaceLedsLeftExternal', 'FaceLedsLeftInternal', 'FaceLed
sLeftTop', 'FaceLedsRightBottom', 'FaceLedsRightExternal', 'FaceLedsRightInternal', 'FaceLedsRightTo
p', 'FaceLedsTop', 'LeftEarLeds', 'LeftEarLedsBack', 'LeftEarLedsEven', 'LeftEarLedsFront', 'LeftEar
LedsOdd', 'LeftFaceLeds', 'LeftFaceLedsBlue', 'LeftFaceLedsGreen', 'LeftFaceLedsRed', 'RightEarLeds'
, 'RightEarLedsBack', 'RightEarLedsEven', 'RightEarLedsFront', 'RightEarLedsOdd', 'RightFaceLeds', '
RightFaceLedsBlue', 'RightFaceLedsGreen', 'RightFaceLedsRed']
```

---

## 全てのLEDを初期化する

AllLedsグループは全てのLEDを含んでいます。 `.reset()` を使って初期化しましょう。

```
>>> leds.reset('AllLeds')
>>>
```

---

## 顔のLEDを光らせる

```
>>> leds.fadeRGB('FaceLeds', 0xffb361, 0.1)
```








## Pythonのインストール

- Python2.6
- PepperのPythonはバージョンが古い
- サードパーティライブラリがサポートを切りつつある

---

## 簡単なPythonチュートリアル

起動

```
$ python
```

---

## 簡単なPythonチュートリアル

1〜10までの数字を表示

```
>>> for ii in range(11): print ii
...
```


---

## あとは使って覚えよう


---

### Editing

- [Pythonデバッグ入門](https://gitpitch.com/TakesxiSximada/presentations/python-debug-tips)


---

## 参考文献

- http://doc.aldebaran.com/2-5/dev/python/install_guide.html
- http://doc.aldebaran.com/1-14/getting_started/helloworld_python.html
