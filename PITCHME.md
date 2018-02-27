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

 APIドキュメント読んだり、ペイロードを調べたり、こちらのDBとの対応を確認したり、実装をあわせたり....

+++

# データの
# 受け渡し

+++

# SOAP ?

+++

# REST API ?

+++

# Other ?

+++

# だいたい
# HTTP(s)で
# 通信する

+++

# そこで

+++

# よく使われるのが

+++

# HTTP Client Tool

+++

# たとえば...

+++

# postman

https://www.getpostman.com/

<img alt="" src="/images/postman.png" width="200">


+++

## Advanced REST client

https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=ja
(Chrome拡張)

<img alt="" src="/images/chrome.png" width="200">

+++

# cUrl

https://curl.haxx.se/

<img alt="" src="/images/curl.png" width="200">

+++

# Telnet

まじで...

+++

## エディタやIDEの
## プラグイン

+++

# vim-rest-console

https://github.com/diepm/vim-rest-console
(Vim)

<img alt="" src="/images/vim.png" width="200">

+++

# rester-sublime-http-client

https://github.com/pjdietz/rester-sublime-http-client
(Sublime)

<img alt="" src="/images/sublime.png" width="200">

+++

# vscode-restclient

https://github.com/Huachao/vscode-restclient
(VS Code)

<img alt="" src="/images/vscode.png" width="200">

+++

<img alt="" src="/images/emacs-gnu.png" width="700">

+++

# Emacs

<img alt="" src="/images/emacs.png" width="200">

+++

Emacsには古の時代からhttp-modeがある

+++

ただhttp-modeはできないことも多い

+++

# restclient.el

https://github.com/rest-client/rest-client

+++

### HTTP REST client tool for emacs
### emacsのためのHTTP RESTクライアントツール

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

<img alt="" src="/images/turing.png" width="400">

+++

env.el は git には含めず env.el.example として配布

+++

まとめ

+++

- 送信スクリプトをgitに入れることで検証がしやすくなる
- レスポンスも送信スクリプトに近い位置にあるとイメージが付きやすい
- なるべく実リクエストに近い形式のものが良い
- チューリング完全大事

+++

# 結論

+++

### 手に馴染んだもの
### を使えば良い

おわり
