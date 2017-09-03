# PythonデバッグTips

---

## print()でデバッグ

print()関数を使って確認したい値をstdoutに出力することでデバッグします。これで解決できるのであれば、それに越したことはありません。

FizzBuzzをデバッグします。今回は1から20までの数値を使ってFizzBuzzを出力したいとします。以下のコードには明らかなバグがあります。わかりますか?

example_fizzbuzz_buggy.py::

```
for ii in range(1, 21):
    if ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    elif ii % 15 == 0:
        print('FizzBuzz')
    else:
        print(ii)

```

これを実行するとexample_fizzbuzz.pyは次のメッセージを表示します。

```
$ python example_fizzbuzz.py
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
16
17
Fizz
19
Buzz
```

何かおかしいですね。`FizzBuzz` という表示が1個もありません。15の場合は`FizzBuzz`を表示するべきです。15の時の挙動を確認するためにprint()を追加してみます。

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

`追加` とコメントした行が追加したprint()です。以下のデバッグメッセージを出力するためにコードを追加しました。

- 現在の数値を `CUURENT: 1` のように表示する
- 数値が15で割り切れた時 `HIT` と表示する

では実行します。

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

`CURRENT: 15` の時は `Fizz` を表示していて、`HIT` は表示していません。ということは `if ii % 3 == 0:` のブロックを実行しており `elif ii % 15 == 0:` のブロックは実行していないことがわかります。ii が 15の場合は当然3で割り切れるので `if ii % 3 == 0:` はTrueになり、その後ろの `elif ii % 15 == 0:` が `elif` のため実行されていません。`ii % 15 == 0` は他の条件よりも先に分岐しなければならないことがわかったのでコードを直します。

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

15の場合、`HIT` と `FizzBuzz` を表示しています。良さそうですね。バグが取り除かれました。あとは先ほど追加されたprint()を削除します。最終的なコードはこのようになります。

example_fizzbuzz.py::

```
for ii in range(1, 21):
    if ii % 15 == 0:
        print('FizzBuzz')
    elif ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    else:
        print(ii)
```

この手法はどのプログラミング言語でもよく使われるものです。そして最後のprint()を削除し忘れるというのもよくやってしまいがちです。忘れず削除するようにしましょう。

---

## pdbを使って1行ずつプログラムの動きを確認する

print()を使ってデバッグではデバッグメッセージをstdoutに出力することでプログラムがどのように動くかを確認しました。単純なプログラムであれば処理を追いかけられますが、複雑になってくるとデバッグメッセージだけでは動きがわかりにくくなります。[pdb](http://docs.python.jp/3/library/pdb.html) を使うとプログラムを1行ずつ確認しながら実行したり、その時の変数の値を確認できるため、よりプログラムの処理を追いかけやすくなります。

では先ほどの不具合入りの `example_fizzbuzz_buggy.py` をpdbを使って実行します。
pdbは標準ライブラリなのでpipでインストールする必要はありません。

```
$ python -m pdb example_fizzbuzz_buggy.py
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(1)<module>()
-> for ii in range(1, 21):
(Pdb)
```

Pythonの引数に `-m pdb` を追加します。pdbで実行したスクリプトは最初に実行するコードで停止し、入力を待ちます。ここでpdbコマンドを指定してENTERを入力することで、デバッガを操作します。pdbコマンドの詳細は [27.3. pdb — Python デバッガー — Python 3.5.2 ドキュメント](http://docs.python.jp/3/library/pdb.html#debugger-commands) で解説されています。

1行ずつ実行するには n (nextの意味) を入力します。

```
(Pdb) n
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb)
```

pdbは1行実行し、次に実行する行を表示しました。

この時表示された `> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()` は次のフォーマットをしています。

`> ファイルパス(実行している行数)関数名()`

今回は関数にしていないので関数名の所は `<module>` という表示になっています。(実際には\_\_name\_\_の値を表示します)

ENTERだけ(コマンドの指定なし)の場合は、1個前のpdbコマンドを実行することになります。
そのためもう一行処理させたい場合は、ENTERを入力します。

```
(Pdb)
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(4)<module>()
-> elif ii % 5 == 0:
(Pdb)
```

l (listの意味) を使うと現在どこの行を実行しているか確認できます。

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
(Pdb)
```

`->` がマークされている行を次に実行します。
1行ずつではなく処理を進めたい場合は、c (continueの意味) を指定します。

```
(Pdb) c
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
16
17
Fizz
19
Buzz
The program finished and will be restarted
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(1)<module>()
-> for ii in range(1, 21):
```

プログラムを最後まで実行しました。最後までプログラムを処理するとpdbは `The program finished and will be restarted` を出力し、プログラムを再実行します。

行数を指定して処理を停止させたい場合、ブレイクポイントを使います。iiが15の時の処理を確認するため、b (breakの意味) コマンドを使ってif文で最初に分岐している2行目にブレイクポイントを設定します。

```
(Pdb) b 2
Breakpoint 1 at /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py:2
(Pdb)
```

これで2行目が処理される前にプログラムが一時停止します。cコマンドを使って処理を進めましょう。

```
(Pdb) c
1
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb)
```

停止しました。p (printの意味) コマンドを使ってiiの値が何かを確認します。

```
(Pdb) p ii
2
(Pdb)
```

2ですね。15の時の処理を確認したいので、cをあと13回実行しましょう。

```
(Pdb) c
2
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Fizz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
4
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Buzz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Fizz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
7
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
8
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Fizz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Buzz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
11
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
Fizz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
13
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) c
14
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) p ii
15
(Pdb)
```

上記ではcを何度も入力しましたが、停止する条件も設定できます。
今回はiiが15の時に停止して欲しいので、次のように条件を指定します。

```
(Pdb) b 2, ii == 15
Breakpoint 3 at /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py:2
(Pdb)
```

そしてcを実行するとiiが15の時だけ停止するので、cを何度も入力する必要はありません。

```
(Pdb) c
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(2)<module>()
-> if ii % 3 == 0:
(Pdb) p ii
15
(Pdb)
```

あとはnで1行ずつ実行し動作を確認します。

```
(Pdb) n
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(3)<module>()
-> print('Fizz')
(Pdb) n
Fizz
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(1)<module>()
-> for ii in range(1, 21):
(Pdb)
```

3行目が実行されたあと1行目のfor文が処理される(つまり6行目の `elif ii % 15 == 0:` が処理されていない)ことがわかります。

```
(Pdb) list
  1  -> for ii in range(1, 21):
  2 B       if ii % 3 == 0:
  3             print('Fizz')
  4         elif ii % 5 == 0:
  5             print('Buzz')
  6         elif ii % 15 == 0:
  7             print('FizzBuzz')
  8         else:
  9             print(ii)
[EOF]
(Pdb)
```

iiが15の時には `ii % 3 == 0` はTrueなので、このif-elif-elseでは15の時に正しく動作しないことをpdbを使って確認しました。

```
(Pdb) p ii
15
(Pdb) p ii % 3 == 0
True
(Pdb)
```

ブレイクポイントは cl (clearの意味) を使って削除します。

```
(Pdb) cl
Clear all breaks? yes
Deleted breakpoint 3 at /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py:2
(Pdb)
```

呼び出した関数の処理を確認するには、s (stepの意味) を指定します。

example_fizzbuzz_buggy2.py::

```
def fizzbuzz(num):
    if ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    elif ii % 15 == 0:
        print('FizzBuzz')
    else:
        print(ii)

for ii in range(1, 21):
    fizzbuzz(ii)
```

example_fizzbuzz_buggy2.pyでfizzbuzz関数に入ってみます。


```
$ python -m pdb example_fizzbuzz_buggy2.py
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(1)<module>()
-> def fizzbuzz(num):
(Pdb) n
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(11)<module>()
-> for ii in range(1, 21):
(Pdb) n
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(12)<module>()
-> fizzbuzz(ii)
(Pdb) p ii
1
```

ここまでは先ほど解説した内容を使って、12行目のfizzbuzz()呼び出しまで処理を進めています。

次にsを指定してfizzbuzz()の内部で処理を停止させています。

```
(Pdb) s
--Call--
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(1)fizzbuzz()
-> def fizzbuzz(num):
(Pdb) n
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(2)fizzbuzz()
-> if ii % 3 == 0:
(Pdb)
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(4)fizzbuzz()
-> elif ii % 5 == 0:
```

fizzbuzz()の関数が終了したところまで処理を進めるには、r (returnの意味) を指定します。

```
(Pdb) r
1
--Return--
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(9)fizzbuzz()->None
-> print(ii)
(Pdb) n
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy2.py(11)<module>()
-> for ii in range(1, 21):
```

`fizzbuzz()->None` はfizzbuzz()がNoneを返したことを表しています。


---

### コード内に `import pdb; pdb.set_trace()` を記述する

pdbを使うために `python -m pdb` で実行していましたが、これでは起動のオプションを変更しなければなりません。これでは、起動スクリプトを作成していたりPythonを直接呼び出さない場合にpdbを使えません。

pdbはそのためにset_trace()を提供しています。set_trace()が呼び出された時にpdbのデバッグモードに切り替わり、コマンドの入力を待ちます。

example_fizzbuzz_buggy.pyにset_trace()を仕込みます。

example_fizzbuzz_buggy.py::

```
for ii in range(1, 21):
    if ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        import pdb; pdb.set_trace()  # 追加
        print('Buzz')
    elif ii % 15 == 0:
        print('FizzBuzz')
    else:
        print(ii)
```

5行目に `import pdb; pdb.set_trace()` を追加しました。
example_fizzbuzz_buggy.py実行しますが、今回は `-m pdb` は指定しません。

```
$ python  example_fizzbuzz_buggy.py
1
2
Fizz
4
> /working/advent-calendar-2016-python/example_fizzbuzz_buggy.py(6)<module>()
-> print('Buzz')
(Pdb)
```

6行目で停止しました。

```
(Pdb) l
  1     for ii in range(1, 21):
  2         if ii % 3 == 0:
  3             print('Fizz')
  4         elif ii % 5 == 0:
  5             import pdb; pdb.set_trace()
  6  ->         print('Buzz')
  7         elif ii % 15 == 0:
  8             print('FizzBuzz')
  9         else:
 10             print(ii)
[EOF]
(Pdb)
```

set_trace()の次の行で処理が停止しています。
この方法を使えば起動オプションを変更することなくpdbを起動できます。

このデバッグコードはデバッグ終了時には必ず削除しなければなりません。
もし削除し忘れてしまった場合、本番の動作中にpdbが起動し入力待ちになるからです。
print()でのデバッグと違い、必ず実害が発生します。
GitのコミットフックやCIのテストでpdbの混入をチェックすることを勧めます。

`import pdb; pdb.set_trace()` は2つの文が指定されていて、片方はimport文です。
本来であればimport文はファイルの先頭に記述することが好まれますが、
このデバッグコードはデバッグ終了時には必ず消さなければならないため、
消す行を減らすために1行で記述しています。
Pythonの公式ドキュメントにもこのように紹介されており、
慣習的にもそれに習い1行で記述します。


---

## ipdbでデバッグ

ipdbはpdbの機能をIPythonを使って拡張したライブラリです。

ipdbはpipでインストールします。

```
$ pip install ipdb
```

`-m ipdb` をPythonの起動オプションに指定するか、`import ipdb; ipdb.set_trace()` をコード内に記述することで起動します。
コードハイライトされていて見やすいです。

![スクリーンショット 2016-12-24 20.52.10.png](https://qiita-image-store.s3.amazonaws.com/0/36261/c2a80285-a504-692e-3037-f7e6ddbd9c99.png)


タブを押すと属性一覧を表示できます。

![スクリーンショット 2016-12-24 20.52.34.png](https://qiita-image-store.s3.amazonaws.com/0/36261/a4c37b64-50fd-0d15-2c3a-069e8fe6884c.png)

その他、使用方法はpdbとほぼ同じです。

---

## bpdbでデバッグ

bpdbはpdbの機能をBPythonを使って拡張したライブラリです。
こちらはBPython自体の1機能として提供されています。

bpdbはpipでbpythonをインストールします。

```
$ pip install bpython
```

`-m bpdb` をPythonの起動オプションに指定するか、`import bpdb; bpdb.set_trace()` をコード内に記述することで起動します。
pdbと同様に動作しますが、`B` を入力すると現在のスタックフレームでBPythonが起動します。

![スクリーンショット 2016-12-24 21.16.30.png](https://qiita-image-store.s3.amazonaws.com/0/36261/b9413100-e2c8-551b-c192-059be3ba381d.png)

BPythonの終了は `C-d` です。

---

## pudbでデバッグ

[PuDB](https://mathema.tician.de/debug-python-in-style/) はコンソール上で使える高機能なデバッガです。

インストールします。

```
pip install pudb
```

インストールするとpudb3というコマンド(Python3の場合)が使えるようになります。
pudb3に実行したいファイルパスを指定することで起動します。

```
$ pudb3 example_fizzbuzz_buggy.py
```

デバッガのペインはpdbの操作と同じです。`C-x` でデバッガのペインとインタラクティブシェルのペインを行き来できます。

![スクリーンショット 2016-12-25 0.15.41.png](https://qiita-image-store.s3.amazonaws.com/0/36261/b60e9474-debb-cb2f-2377-0c180702141b.png)


テーマなどを設定でき、設定値は~/.config/pudb/pudb.cfgに保存しています。

~/.config/pudb/pudb.cfg::

```
[pudb]
breakpoints_weight = 1
current_stack_frame = top
custom_stringifier =
custom_theme =
display = auto
line_numbers = True
prompt_on_quit = True
seen_welcome = e027
shell = classic
sidebar_width = 0.5
stack_weight = 1
stringifier = type
theme = dark vim
variables_weight = 1
wrap_variables = True
```

---

## PyCharmでデバッグ

[PyCharm](https://www.jetbrains.com/pycharm) はJetBrains社が開発したPythonのIDEです。GUI操作でデバッガを操作できます。とても直感的に操作することができ素晴らしいです。インストーラは https://www.jetbrains.com/pycharm/download/ からダウンロードできます。

ファイルを開き、ブレイクポイントを設定してみます。

![スクリーンショット 2016-12-25 0.37.53.png](https://qiita-image-store.s3.amazonaws.com/0/36261/31a5a886-5c37-7ca9-1718-88c38fed7498.png)


行番号表示の右側をクリックすると赤丸が出現します。これがデバッガです。VSとかEclipseとかと同じですね。

実行はメニューから [Run] > [Debug]、 (もしくは虫マーク
)をクリックします。

![スクリーンショット 2016-12-25 0.41.05.png](https://qiita-image-store.s3.amazonaws.com/0/36261/bb58c79b-ea17-37f2-79a6-f77a4cd28052.png)

虫マーク

![スクリーンショット 2016-12-25 0.41.26.png](https://qiita-image-store.s3.amazonaws.com/0/36261/60033b9a-7aeb-97aa-143b-222e9b9b7a83.png)


実行するとブレイクポイントで止まり、スタックフレームや変数がペインに表示されます。

![スクリーンショット 2016-12-25 0.38.40.png](https://qiita-image-store.s3.amazonaws.com/0/36261/f58ba432-f7ed-ceab-d989-62e69aa5874d.png)



細かい操作はアイコンが有効になるのでそれをクリックすれば操作できるし、マウスオーバーすれば何を行うアイコンかを表示します。


![スクリーンショット 2016-12-25 0.42.37.png](https://qiita-image-store.s3.amazonaws.com/0/36261/e726f6af-4732-7e71-bbb1-0e662a23d4f6.png)


またProfessional Editionではリモートデバッグ機能が使えます。

---

## いろんなシーンでデバッグする

---

## unittestでデバッガを使いたくなったら

unittestでエラーになるけど原因がわからない場合、testコードでデバッグしたくなります。
その場合はテストコード内に `pdb.set_trace()` を仕込み、pdbを起動できます。

例えば以下のテストコードでテスト実行時にpdbを起動します。

test_main.py::

```
from unittest import TestCase


def create_message(count):
    return 'Fish: {}'.format(count)


class SimpleTest(TestCase):
    def test_it(self):
        import pdb; pdb.set_trace()  # デバッグコード
        msg = create_message(1)
        self.assertEqual(msg, 'Fish: 1')
```

unittestを実行するとpdbが起動します。

```
$ python -m unittest
> /working/advent-calendar-2016-python/test_main.py(11)test_it()
-> msg = create_message(1)
(Pdb) list
  6
  7
  8     class SimpleTest(TestCase):
  9         def test_it(self):
 10             import pdb; pdb.set_trace()  # デバッグコード
 11  ->         msg = create_message(1)
 12             self.assertEqual(msg, 'Fish: 1')
[EOF]
(Pdb)
```

## noseでデバッガを使いたくなったら

[nose](https://nose.readthedocs.io/en/latest/) はよく使われるテストフレームワークです。
先ほどのようにテストを途中でpdbを使って停止させる場合、`--nocapture` を指定します。

```
$ nosetests --nocapture
> /working/advent-calendar-2016-python/test_main.py(11)test_it()
-> msg = create_message(1)
(Pdb)
```

またエラーや失敗した時にpdbを起動するための `--pdb`、 `--pdb-failures`、`--pdb-errors` も提供されています。

```
$ nosetests --pdb
> /Users/sximada/ng2/var/lib/miniconda3/envs/py3.5.2/lib/python3.5/unittest/case.py(665)fail()
-> raise self.failureException(msg)
(Pdb)
```

noseのドキュメントには `Warning nose itself supports python 3, but many 3rd-party plugins do not!` と記述がある通り、
nose自体ではなく、noseのpluginのPython3対応が進んでいないようです。

---

## pytestでデバッガを使いたくなったら

[pytest](http://docs.pytest.org/en/latest/) もnose同様よく使われるテストフレームワークです。
[pytest](http://docs.pytest.org/en/latest/) はそのまま実行すれば、set_trace()実行時にpdbが起動します。

```
$ pytest
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /working/advent-calendar-2016-python, inifile:
plugins: celery-4.0.0
collected 1 items

test_main.py
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> /working/advent-calendar-2016-python/test_main.py(11)test_it()
-> msg = create_message(1)
(Pdb)
```

`--pdb` を指定することでエラー時にデバッガを起動できます。

```
$ pytest --pdb
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /working/advent-calendar-2016-python, inifile:
plugins: celery-4.0.0
collected 2 items

test_main.py F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

self = <test_main.SimpleTest testMethod=test_error>

    def test_error(self):
        msg = create_message(1)
>       self.assertEqual(msg, 'ERROR')
E       AssertionError: 'Fish: 1' != 'ERROR'
E       - Fish: 1
E       + ERROR

test_main.py:15: AssertionError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> /Users/sximada/ng2/var/lib/miniconda3/envs/py3.5.2/lib/python3.5/unittest/case.py(665)fail()
-> raise self.failureException(msg)
(Pdb)
```

---

## Djangoでデバッガを使いたくなったら

[Django](https://www.djangoproject.com/) はよく使われるウェブフレームワークです。
[Django](https://www.djangoproject.com/) でpdbを使うことは
開発サーバ(`manage.py runserver`)であれば何も難しくありません。

プロジェクトを作成してpdbを起動してみます。

プロジェクトの構成は以下の通りです。

```
$ tree proj
proj
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py
```

proj/urls.pyは次のように記述します。


```
from django.conf.urls import url
from django.http import HttpResponse


def top_view(request):
    import pdb; pdb.set_trace()
    return HttpResponse('OK')

urlpatterns = [
    url(r'^$', top_view),
]
```

`/` にアクセスすると`OK`とリクエストを返すViewを定義しています。
(ファイルを分割するのが面倒だったのでviewもurls.pyに記述しています)
View関数内にはpdb.set_trac()を記述しています。

runserverで開発サーバを起動します。

```
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
December 24, 2016 - 13:45:26
Django version 1.11.dev20161224024349, using settings 'proj.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

URLにリクエストを送信します。

```
$ curl http://127.0.0.1:8000/
```

開発サーバはpdb.set_trace()によってpdbを起動し入力を待ちます。

```
> /working/advent-calendar-2016-python/proj/urls.py(7)top_view()
-> return HttpResponse('OK')
(Pdb)
```

後はデバッグするだけです。リクエストオブジェクトの中身を確認も確認できます。他のWAFも同様にpdbでデバッグできることが多いです。

---

## gunicornでデバッガを使いたくなったら

[gunicorn](http://gunicorn.org/) はよく使われるWSGI HTTP Serverです。
先ほどのDjango Projectを [gunicorn](http://gunicorn.org/) で実行します。

```
$ gunicorn proj.wsgi:application
[2016-12-24 22:53:59 +0900] [8915] [INFO] Starting gunicorn 19.6.0
[2016-12-24 22:53:59 +0900] [8915] [INFO] Listening at: http://127.0.0.1:8000 (8915)
[2016-12-24 22:53:59 +0900] [8915] [INFO] Using worker: sync
[2016-12-24 22:53:59 +0900] [8918] [INFO] Booting worker with pid: 8918
```

URLにリクエストを送信します。

```
$ curl http://127.0.0.1:8000/
```

pdb.set_trace()によってpdbが起動します。

```
> /working/advent-calendar-2016-python/proj/urls.py(7)top_view()
-> return HttpResponse('OK')
(Pdb)
```

先ほどのDjangoの開発サーバと同じです。

---

### タイムアウトに気をつける

Gunicornはリクエストをタイムアウトにする設定がありデフォルトで30秒です。pdbを起動してデバッグ中に `(Pdb) [2016-12-24 23:09:37 +0900] [9102] [CRITICAL] WORKER TIMEOUT (pid:9115)` を表示して
pdbが終了してしまう場合はリクエストがタイムアウトとして扱われているので、`--timeout` でタイムアウトの値を大きく設定して実行します。

```
$ gunicorn proj.wsgi:application --timeout 9999999
[2016-12-24 23:13:11 +0900] [9126] [INFO] Starting gunicorn 19.6.0
[2016-12-24 23:13:11 +0900] [9126] [INFO] Listening at: http://127.0.0.1:8000 (9126)
[2016-12-24 23:13:11 +0900] [9126] [INFO] Using worker: sync
[2016-12-24 23:13:11 +0900] [9130] [INFO] Booting worker with pid: 9130
> /working/advent-calendar-2016-python/proj/urls.py(7)top_view()
-> return HttpResponse('OK')
(Pdb)
```

---

## Celeryでデバッガを使いたくなったら

[Celery](https://docs.celeryproject.org) はよく使われるタスクキューです。
Brokerとして今回はRedisを使うので起動しておきます。

```
$ nohup redis-server 2>&1 > /dev/null &
[1] 9384
```

tasks.pyを作成し、add()タスクを定義します。今回はこのadd()タスクをデバッグしたいとします。


tasks.py::

```
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    import pdb; pdb.set_trace()
    return x + y
```

workerを起動します。

```
$ celery -A tasks.app worker

 -------------- celery@ng-2.local v4.0.0 (latentcall)
---- **** -----
--- * ***  * -- Darwin-16.1.0-x86_64-i386-64bit 2016-12-24 23:23:27
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x1042b4940
- ** ---------- .> transport:   redis://127.0.0.1:6379//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
```

 別のターミナルでタスクを発火します。

```
>>> import tasks
>>> tasks.add.delay(1, 2)
<AsyncResult: a07399f4-e28a-4471-b57d-30ce1cb3abf4>
>>>
```

workerを実行しているターミナルではbdb.BdbQuit例外が発生してしまいます。

```
[2016-12-24 23:24:50,006: WARNING/PoolWorker-4] > /working/advent-calendar-2016-python/tasks.py(9)add()
-> return x + y
[2016-12-24 23:24:50,007: WARNING/PoolWorker-4] (Pdb)
[2016-12-24 23:24:50,061: ERROR/PoolWorker-4] Task tasks.add[a07399f4-e28a-4471-b57d-30ce1cb3abf4] raised unexpected: BdbQuit()
Traceback (most recent call last):
  File "/Users/sximada/ng2/var/lib/miniconda3/envs/py3.5.2/lib/python3.5/site-packages/celery/app/trace.py", line 368, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/Users/sximada/ng2/var/lib/miniconda3/envs/py3.5.2/lib/python3.5/site-packages/celery/app/trace.py", line 623, in __protected_call__
    return self.run(*args, **kwargs)
  File "/working/advent-calendar-2016-python/tasks.py", line 9, in add
    return x + y
  File "/working/advent-calendar-2016-python/tasks.py", line 9, in add
    return x + y
  File "/Users/sximada/ng2/var/lib/miniconda3/envs/py3.5.2/lib/python3.5/bdb.py", line 48, in trace_dispatch
    return self.dispatch_line(frame)
  File "/Users/sximada/ng2/var/lib/miniconda3/envs/py3.5.2/lib/python3.5/bdb.py", line 67, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
```

実はCeleryのデバッグ方法は http://docs.celeryproject.org/en/latest/userguide/debugging.html に記載があります。
pdbはそのまま使えず、 celery.contrib.rdbを使う必要があり、telnet経由でデバッガを使います。tasks.pyを修正します。

tasks.py::

```
from celery import Celery
from celery.contrib import rdb

app = Celery('tasks', broker='redis://127.0.0.1/')


@app.task
def add(x, y):
    rdb.set_trace()
    return x + y
```

タスクを再発火します。

```
>>> import tasks
>>> tasks.add.delay(1,2)
<AsyncResult: 42b88871-a679-492f-bfc9-1f86043dab33>
>>>
```

するとworkerは `Remote Debugger:6900: Waiting for client...` というメッセージを表示します。
このポート番号にtelnetでアクセスします。

```
$ telnet 127.0.0.1 6900
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
> /working/advent-calendar-2016-python/tasks.py(10)add()
-> return x + y
(Pdb) p x
1
(Pdb) p y
2
(Pdb)
```

pdbが入力待ちしています。後はpdbの操作と同様です。
タスクが終了するとworkerはポートを閉じます。
複数回実行する場合は、その都度telnetで接続し直さなければなりません。

Celeryの場合はadd(1, 2)だと通常の関数実行になるので、それでデバッグしていくのも手です。
ただそれでもCeleryのコードは実行されるので、タスクではない関数として実行できる状態にしておくと、
Celeryの問題なのかの切り分けがしやすくなります。

## jupyter notebookでデバッガを使いたくなったら

jupyter notebookには `%debug` マジックコマンドが提供されていて、これによりpdbを起動できます。
以下は requests.get('http://example.com') をpdbでデバッグしています。

![スクリーンショット 2016-12-25 0.05.23.png](https://qiita-image-store.s3.amazonaws.com/0/36261/3bf79b4a-ba00-3aa3-b165-422d0efff8b2.png)

## CircleCIでデバッガを使いたくなったら

[Circle CI](https://circleci.com/) はよく使われるCIサービスです。
[Circle CI](https://circleci.com/) 上で実行しているテストがエラーして、その原因が特定できないことがあります。
その場合、`Rebuild with SSH` を選択してビルドすると、ビルドコンテナにSSHでログインし挙動を確認できます。

![スクリーンショット 2016-12-24 22.20.56.png](https://qiita-image-store.s3.amazonaws.com/0/36261/ba41bf83-8e9d-73ee-b009-68c8d149d59d.png)


ホームディレクトリにリポジトリをcloneしているので、そこでコード内に `pdb.set_trace()` を仕込んで、
手動でテストを実行することで、エラーの原因を特定しやすくなります。

---

## staging環境でデバッガを使いたくなったら

これは別にPythonに限った話ではないのですが、sshでログインできるstaging環境がある場合、
staging環境上でpdbを実行したくなりますよね。

例えばDjangoアプリケーションなら、
staging上でpdb.set_trace()を記述して手動で開発サーバを適当なポート番号で起動し、
ssh port forwardで開発サーバに繋げられるようにするのが手っ取り早いです。

```
[staging]$ python manage.py runserver 4649
```

ssh port forwardでlocalhost:8000をstaging:4649に接続します。

```
$ ssh -L 8000:localhost:4649 staging
```

後はlocalhostでテストしているようにリクエストを送信します。

---

## production環境でデバッガを使いたくなったら

絶対にやめましょう。事故ります(宣言)。
RC環境があるならやってもいいかもしれませんが、
それでも細心の注意を払わないと目も当てられないことになります。
