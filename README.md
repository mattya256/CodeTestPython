# CodeTestPython

## 目的
Python3のプログラムのコードを入力すると計算時間や変数の変化などを出力することができます。
主にAtCoderなどでのPythonの計算量理解、動作理解を支援することを目的として作成しました。

## 環境
Python : 3.9.6

flask 2.1.2

## 動作手順

route.pyを起動し、http://127.0.0.1:8000
にアクセスします。

今回はAtCoderの問題(https://atcoder.jp/contests/abc258/tasks/abc258_c)
を想定します。

「Code:」のテキストボックスにテストしたいコード、「TestCase:」にinputを入力します。

その後、Runを押して実行します。実行時の変数の変化を全て出力することもできますが、計算量が大きいため必要に応じてチェックボックスにチェックを入れてください。

![image](https://user-images.githubusercontent.com/96227270/197346758-839d7b69-0b89-4b43-bb20-c9794babb407.png)
画像1 : 実行時の出力例

実行にかかった時間、printで出力した値が確認できます。
実行にかかった時間はPython3での実行時間なので、AtCoderでよく使用されるPypy3の実行時間とは少し異なる可能性があります。

実行時に変数の一覧を取得するにチェックを入れて置き、コードの表記で変数表示にするとプログラムのどの部分で変数が変化したかを可視化できます。
![image](https://user-images.githubusercontent.com/96227270/197346828-2dafe761-596d-48af-8df2-183e87eeec5f.png)
画像2 : 変数の可視化

これにより意図したとおりにプログラムが動いているか、どこで誤った挙動をしているかを確認できます。

計算量や実行時間も可視化できます。
どの行でどの程度実行時間がかかっているか、どの行が何回呼び出されているか、その行の処理に平均何秒かかっているかを可視化できます。

![image](https://user-images.githubusercontent.com/96227270/197347073-48ea5434-6c89-4380-a7f3-f45e8ee45545.png)
画像3 : 実行時間の長い行の可視化

![image](https://user-images.githubusercontent.com/96227270/197347099-a6ad56ad-f320-4f8f-97e7-e63dffb65df5.png)
画像4 : 呼び出し回数の多い行の可視化

![image](https://user-images.githubusercontent.com/96227270/197347114-44cac6bc-ff55-46cb-8831-706efcb926e2.png)
画像5 : 一回の呼び出し当たりの実行時間

呼び出し回数と一回の呼び出し当たりの実行時間を比較することで、ループ回数が多く計算量が増加しているのか、計算量の大きい関数を使用しているのかを区別できます。

## 今後の改良
変数の取得などで計算量が多くなってしまっているため、最適化を行いたいです。
またAtCoderの実行環境に合わせ、Pypy3での実行にも対応したいです。

現在は入力されたコードを書き替え、計算量を取得してからexecコマンドで実行する形式にしています。
このため任意のコードを簡単に実行できてしまうことから、セキュリティの問題があり一般公開が難しいです。
セキュリティの問題を修正し、Webアプリとして公開できるように改善していきたいです。

