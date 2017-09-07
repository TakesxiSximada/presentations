---

## 🍅 今日のアジェンダ 🍅

---

- デバッグとは
- 実際にデバッグする |
- 様々なデバッガの特徴 |
- 様々な環境でのデバッグ方法 |
- デバッグ関連の失敗談と対処方法 |

---

- 🍅 デバッグとは
- 実際にデバッグする
- 様々なデバッガの特徴
- 様々な環境でのデバッグ方法
- デバッグ関連の失敗談と対処方法

---

# デバッグとは...

---


デバッグ（debug）とは、コンピュータプログラムや電気機器中のバグ・欠陥を発見および修正し、動作を仕様通りのものとするための作業である。

Wikipediaより

---

バグ(プログラムの意図していない挙動)を...

- 発見する |
- 修正する |

---

簡単ですね？

---

- ~~デバッグとは~~
- 🍅 実際にデバッグする
- 様々なデバッガの特徴
- 様々な環境でのデバッグ方法
- デバッグ関連の失敗談と対処方法

---

# 実際にデバッグする

---

### fizzbuzz

- 1から20までの数字を標準出力に表示
- 3の倍数なら数字の代わりにFizzと表示
- 5の倍数なら数字の代わりにBuzzと表示
- 3と5の倍数なら数字の代わりにFizzBuzzと表示

※今回は1から20までを実施

---?code=fizzbuzz.py

※バグが含まれています |

---

実行してみる

---?code=fizzbuzz_stdout_1.log


+++?code=fizzbuzz_stdout_2.log

---

- `FizzBuzz` という表示が1個もない
- どこが悪いんだろう？？？ |

---

### デバッグのために表示を追加

```
for ii in range(1, 21):
    print('CURRENT: {}'.format(ii))  # 追加
    if ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    elif ii % 15 == 0:
        print('HIT')  # 追加
        print('FizzBuzz')
    else:
        print(ii)

```

@[2](現在の数値を表示)
@[8](3の倍数かつ5の倍数の条件に入ったらHITを表示)

---

##### 実行

```
$ python  example_fizzbuzz.py
CURRENT: 1
1
CURRENT: 2
2
CURRENT: 3
Fizz
CURRENT: 4
4
CURRENT: 5
Buzz
CURRENT: 6
Fizz
CURRENT: 7
7
CURRENT: 8
8
CURRENT: 9
Fizz
CURRENT: 10
Buzz
```

見やすい|

+++

##### 実行

```
CURRENT: 11
11
CURRENT: 12
Fizz
CURRENT: 13
13
CURRENT: 14
14
CURRENT: 15
Fizz
CURRENT: 16
16
CURRENT: 17
17
CURRENT: 18
Fizz
CURRENT: 19
19
CURRENT: 20
Buzz
```

@[9-10](15がFizz！！(正しくはFizzBuzz))


---

- なんで？？？

---

##### 処理を追いかける

```
for ii in range(1, 21):
    print('CURRENT: {}'.format(ii))  # 追加
    if ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    elif ii % 15 == 0:
        print('HIT')  # 追加
        print('FizzBuzz')
    else:
        print(ii)
```

@[1](iiが15の時)
@[3](15 % 3 == 0)
@[4](実行されてしまう)
@[5](最初のifが実行されたので実行されない)
@[7](最初のifが実行されたので実行されない)
@[10](最初のifが実行されたので実行されない)
@[1](次のターン！！)

---

# 🍅バグ🍅

---

3の倍数と5の倍数は一番最初に調べる必要がありそう。

---

##### コードを修正する

```
for ii in range(1, 21):
    print('CURRENT: {}'.format(ii))
    if ii % 15 == 0:
        print('HIT')
        print('FizzBuzz')
    elif ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    else:
        print(ii)
```

@[3-4](一番最初に15を調べるように修正)

---

###### 実行

```
$ python example_fizzbuzz.py
CURRENT: 1
1
CURRENT: 2
2
CURRENT: 3
Fizz
CURRENT: 4
4
CURRENT: 5
Buzz
CURRENT: 6
Fizz
CURRENT: 7
7
CURRENT: 8
8
CURRENT: 9
Fizz
CURRENT: 10
Buzz
```

+++

###### 実行

```
CURRENT: 11
11
CURRENT: 12
Fizz
CURRENT: 13
13
CURRENT: 14
14
CURRENT: 15
HIT
FizzBuzz
CURRENT: 16
16
CURRENT: 17
17
CURRENT: 18
Fizz
CURRENT: 19
19
CURRENT: 20
Buzz
```

@[9-11](LGTM)

---

printデバッグ

---

- 標準出力に値を出力することでデバッグ
- もっとも基本的な手法 |
- どの言語でもよく使われる |

---





### デバッグとは...

- コード量が多かったら...
- 仕様が複雑だったら...

---

### まとめ

今回は次のことを学びました。

- [x] デバッグとは何か
- [x] printデバッグの方法と考え方
- [x] 様々なデバッガ特徴 (pdb, ipdb, bpdb, pudb, pycharm)
- [x] 様々な環境でのデバッグ方法(Django, Gunicorn, Celery, Jupyter notebook, pytest, nose, CircleCI)
- [x] デバッグ関連の失敗談と対処方法

### 終わり

Enjoy DEBUG！！


##



- [ ] デバッグとは何か
- [ ] デバッグする
- [ ] デバッグでよく用いられるツールのメリット/デメリット
  - print
  - pdb
  - ipdb
  - bpdb
  - pudb
  - pycharm
- [ ] 様々な環境でのデバッグ
  - Djangoをデバッグする
  - Gunicornで動いているPythonコードをデバッグする
  - Celeryタスクをデバッグする
  - Jupyter Notebbook上でデバッグする
  - テストコードをデバッグする
  - CI環境上でデバッグする(CircleCI)
  -
- [ ] デバッグでの失敗談
  - pdbをコードの中に入れてしまった
  - デバッグしにくいコードになってしまった
  - loggerでちゃんとログを出しておけばデバッガでデバッグする必要がなかった
- [ ] まとめ



---

# Pycon JP 2017

## Pythonデバッグ入門

---

# デバッグ

今日のテーマはデバッグです。

みなさん、デバッグしていますか？

ここにいるみなさんはPythonを普段書いていたり、これから書こうと思っている人が多いと思います。

Pythonを書いて実行すると、エラーで処理が停止したり、思い通りの動きをしなかったりすることがありますね。

それがバグです。

これはPythonに限らず他の言語でも同じようにバグに遭遇します。

もちろんバグに遭遇しないにこしたことはありませんし、バグを作らないようにするべきです。

誰もバグを好きでつくているわけではありません。

それでもバグは生まれ、潜んでいます。

このバグを探し出し取り除くことをデバッグと言います。

このデバッグの方法を今日は色々と紹介していきます。

---
