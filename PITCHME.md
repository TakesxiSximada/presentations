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

# 簡単

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

※バグが含まれています

---

実行してみる

---?code=fizzbuzz_stdout_1.log


+++?code=fizzbuzz_stdout_2.log

---

- `FizzBuzz` という表示が1個もない
- どこが悪いのかを調べる |

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

見やすい

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

@[9-10](15がFizz！！正しくはFizzBuzz)


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

### 3の倍数と5の倍数は
### 一番最初に調べる必要がありそう

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

@[3-5](一番最初に15を調べるように修正)

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

# 🍅バグを修正できたああああああああ🍅

---

- ~~デバッグとは~~
- ~~実際にデバッグする~~
- 🍅 様々なデバッガの特徴
- 様々な環境でのデバッグ方法
- デバッグ関連の失敗談と対処方法

---

##### 僕らの武器
### printデバッグ

---

### printデバッグの特徴と問題点

- 簡単で手っ取り早い
- 単純な処理は追いかけられる |
- 複雑な処理を追いかけづらい |
- 表示してもよくわからないobjectもある |
- classのインスタンスとか
- 例 `<__main__.Testing object at 0x108c4e160>` |

 ⬇

- 1行ずつ処理を確認しながら実行したい |
- 実行中の変数も確認したい |

---

# pdb

---

### pdb とは

- Python標準のデバッガ
- インストール不要
- CLI操作でデバッグを実行
- gdbに似ている (Cのデバッガ)

---

# 実行

```
$ python -m pdb fizzbuzz.py
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(1)<module>()
-> for ii in range(1, 21):
(Pdb)
```

@[1](スクリプト実行時に `-m pdb` を指定)
@[3-4](スクリプトの最初の処理で停止)

---

### 1行進む

```
(Pdb) n
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb)
```

@[1](n RETを入力)
@[3-4](1行実行し停止)

---

### 表示の解説

```
> /src/presentations/fizzbuzz.py(2)<module>()
```

- `> ファイルパス(実行している行数)関数名()`
- 今回は関数にしていないので関数名の所は `<module>` という表示
- 実際には\_\_name\_\_の値を表示


---

### 前回と同じ処理を実行

```
(Pdb)
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(4)<module>()
-> elif ii % 5 == 0:
(Pdb)
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(6)<module>()
-> elif ii % 15 == 0:
(Pdb)
```

@[1](RET)
@[2-3](実行)
@[4](RET)
@[5-6](実行)


---

### 現在どこの行を実行しているかを確認


```
(Pdb) l
  1     for ii in range(1, 21):
  2         if ii % 3 == 0:
  3             print('Fizz')
  4  ->     elif ii % 5 == 0:
  5             print('Buzz')
  6         elif ii % 15 == 0:
  7             print('FizzBuzz')
  8         else:
  9             print(ii)
[EOF]
```

@[1](lを入力)
@[5](次に実行される行)

---

### 処理を続行させる

```
(Pdb) c
2
Fizz
4
Buzz
〜 省略 〜
Fizz
19
Buzz
The program finished and will be restarted
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(1)<module>()
-> for ii in range(1, 21):
(Pdb)
```

@[1](cを入力)
@[2-9](処理が続行される)
@[10-13](再び最初から実行)

---

### break point

```
(Pdb) b 2
Breakpoint 1 at /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py:2
(Pdb) c
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb)
```

@[1](b [行番号]を入力)
@[2](2行目にbreak pointが作成される)
@[3](cで処理を続行)
@[5-6](break pointで処理が停止)

---

### 値の表示

```
(Pdb) p ii
1
(Pdb)
```

@[1](pでiiを表示する)
@[2](1が表示される)
@[3](処理が停止)

---

### pdbを使ってFizzBuzzをデバッグ


```
$ python -m pdb fizzbuzz.py
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(1)<module>()
-> for ii in range(1, 21):
(Pdb) l
  1  -> for ii in range(1, 21):
  2         if ii % 3 == 0:
  3             print('Fizz')
  4         elif ii % 5 == 0:
  5             print('Buzz')
  6         elif ii % 15 == 0:
  7             print('FizzBuzz')
  8         else:
  9             print(ii)
[EOF]
```

+++

### 続き

```
(Pdb) b 2
Breakpoint 1 at /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py:2
(Pdb) c
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
1
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
2
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
c(Pdb) c
Fizz
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
c(Pdb) c
4
```

+++

### 続き

```
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Buzz
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
c(Pdb) c
Fizz
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
c(Pdb) c
7
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
8
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Fizz
```

+++

### 続き

```
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Buzz
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
11
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Fizz
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
13
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
14
```

+++

### 続き

```
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) p ii
15
(Pdb) n
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(3)<module>()
-> print('Fizz')
(Pdb) list
  1     for ii in range(1, 21):
  2 B       if ii % 3 == 0:
  3  ->         print('Fizz')
  4         elif ii % 5 == 0:
  5             print('Buzz')
  6         elif ii % 15 == 0:
  7             print('FizzBuzz')
  8         else:
  9             print(ii)
[EOF]
(Pdb) n
Fizz
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(1)<module>()
-> for ii in range(1, 21):
(Pdb)
```

@[2-7](おかしな処理を確認)

---

# ！！

---

c RET c RET c RET c RET c RET
c RET c RET c RET c RET c RET
c RET c RET c RET c RET


大変だ...

---

### break pointに条件を指定

```
The program finished and will be restarted
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(1)<module>()
-> for ii in range(1, 21):
(Pdb) b 2, ii == 15
Breakpoint 3 at /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py:2
(Pdb) c
1
2
〜省略〜
13
14
> /Users/sximada/src/github.com/TakesxiSximada/presentations/fizzbuzz.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) p ii
15
(Pdb)
```

@[4](iiが15の時だけ処理を停止)
@[6-11](実行)
@[12-14](停止)

---

### break pointの除去

```
(Pdb) cl
Clear all breaks?
(Pdb)
```

@[1](clで除去)

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
