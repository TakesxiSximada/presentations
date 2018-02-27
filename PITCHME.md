## サービス連携で
## よくやること

しむどん ( @TakesxiSximada )

---

## 自己紹介

- Emacs大好き
- 最近clojure病疾患中
- JK

---

## サービス連携

+++

## どうやって
## やってる？

+++

## SOAP ?
## Rest API ?
## Other ?

+++

# どれもHTTPで通信する

+++

# HTTP Client

+++

# post man ?

https://www.getpostman.com/

+++

# Advanced REST client ?
(Chrome拡張)

https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=ja

+++

## エディタやIDEのプラグインを使っている？

+++

- Vim: vim-rest-console
- Sublime: rester-sublime-http-client
- VS Code: Rest Client Mode

+++


# cUrl ?

https://curl.haxx.se/

+++

# Telnet

まじで...

+++

# Emacs

+++

Emacsには古の時代からhttp-modeがある

+++

ただhttp-modeはできないことも多い

+++

# restclient.el

https://github.com/rest-client/rest-client

+++

# restclient.el

HTTP REST client tool for emacs
emacsのためのHTTP RESTクライアントツール

+++

# インストール

+++

M-x package-istall restclient RET

+++

デモ

+++

# GET

+++

# POST

+++

# DELETE

+++

基本手書き

+++

# XML

+++

# 画像

+++

# cookie

(setq restclient-inhibit-cookies t)

+++

# 変数の扱い

+++

# env.el

+++

# Lispが
# 記述できる

+++

# チューリング完全

+++

env.el は git には含めず env.el.example として配布

+++

まとめ

+++

- 送信スクリプトをgitに入れることで検証がしやすくなる
- レスポンスも送信スクリプトに近い位置にあるとイメージが付きやすい
- なるべく実リクエストに近い形式のものが良い
- 設定がチューリング完全じゃないとダメ

+++

# 結論

+++

### 手に馴染んだもの
### を使えば良い
