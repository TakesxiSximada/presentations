# Mastodon x Python

しむどん ( @sximada )

---

## おまえだれよ

- しむどん ( @sximada )
- 普段mstdn.jpにいる
- EmacsとPythonが大好き
- ときどき🍅配る

---

# 注意

---

## 二コフレの
## あの方とは
## 別人です

---

# 突然ですが

---

# 大発表

---

# 14万トゥート

---

# 超えま
# した！！

---

<img src="/images/14man.png" width="400px">

拍手〜

---

# 今日の目標

---

### 今日の目標

@ul

- 「Pythonでこんなことができるんだ」
- 「Pythonおもしろそうだなあ」
- 「しむどんに5000兆円あげたいなあ」

@ulend

---

## Pythonとは

- プログラミング言語のひとつ
- Webや機械学習の分野でよく使われる
- コードがよみやすい
- ライブラリがいっぱいある (標準/サードパーティ)
- 速くはない

---

# Hello world!

---

### JavaのHello world!


```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

---

### PythonのHello world!

```
print('Hello world!')
```

---

- Javaがダメな言語といっているわけではない
- プログラミング言語には長所や短所がある
- PythonはJavaよりも手軽

---


## どこで
## 使われているの？

---

### Pythonを使っている
### サービスやツール

- Google / Dropbox / Instagram
- Pepper / Blender / Gimp
- Ansible / Sphinx

+++

instagram engineering blog  https://instagram-engineering.com/what-powers-instagram-hundreds-of-instances-dozens-of-technologies-adf2e22da2ad

---

# その他色々

---

## MastodonとPython

---

###  一人のユーザーとして楽しむ

- MastodonはRubyとNode.jsだが
- 利用するという観点で言えばPythonを使っていろいろと遊べる
- 去年一年にMastodon x Pythonでやったことを振りかえる

---

### クライアントを書いた

---

<img src="/images/pao-console.png">

---

<img src="/images/pao-toot.png">

---

<img src="/images/pao.png">

---

<img src="/images/asaga.png">

---

## cmd

- CLIツール用フレームワーク
- 標準ライブラリ
- import cmd

---

## Mastodon.py

- マストドンAPIライブラリ
- サードパーティ製
- pip install Mastodon.py

https://github.com/halcy/Mastodon.py

---

その後これは放棄されて

自作Emacs Clientに発展していきます

---

#### mastodon dev会議での発表資料

<img src="/images/mastodonxemacs.png" width="400px">
https://slideship.com/users/@sximada/presentations/2017/08/NwfdMr4rrtxFPQ2ZQVg6qq/

---

### Twitcasting to Mastodon

---

#### 構成

<img src="/images/cathy.png">

---

#### アプリケーションの作成

<img src="/images/create-twitcasting-app.png">

---

#### Webhookの登録

```
POST https://apiv2.twitcasting.tv/webhooks
Accept: application/json
X-Api-Version: 2.0
Authorization: Basic :TOKEN
Content-Type: application/json

{
    "user_id": ":USER_ID",
    "events": ["livestart"]
}
```

---

#### Zappa

```
$ pip install zappa
$ zappa init
$ zappa deploy
```

---

未収載で流そうかと思ったが、そもそも気づかれたくない人もいるはずなのでセルフDMでしばらく運用し、そのうち使わなくなった...

---

### Tootの可視化

---

<img src="/images/ruikei.png">

---

<img src="/images/month.png">

---

<img src="/images/flow-01.png">


---

### こんな感じで
### 色々遊べる

---

## Pythonを始めるには
## 何からやれば
## 良いんだろう

---

## インストールせずに
## 触わってみる

---

## PythonTutor

http://pythontutor.com/visualize.html#mode=edit

---

## Try Jupyter

http://jupyter.org/try

---

## インストールする

- 公式 https://www.python.org/downloads/
- pyenv
- conda
- homebrew (macOS)

---

# Python2?
# Python3?

---

# Python3!!

---

## まとめ

@ul

- わーい
- Pythonすごーい
- Mastodonたーのしー

@ulend

---

## みんなやろうよ
## Mastodon and Python

おわり
