# RSNP チュートリアル2020 デモンストレーション
<h4> 芝浦工業大学 知能機械システム研究室　加藤宏一朗，松日楽　信人</h4>

本システムをご利用予定の方は，お手数ですが下記の連絡先までご連絡ください．また，改善点などのご意見がある方も，下記の連絡先までご連絡ください．**RSNP(Robot Service Network Protocol)をご利用いただくには，使用条件にご同意していただき，RSi事務局にお問い合わせしていただく必要がありますので，ご注意ください．** RSiとRSNPに関しては以下のURLでご参照ください．RSNPユニットのハードウェア，ソフトウェアの仕様に関しては，以下のURLをご参照ください．  

[RSiとRSNPに関して](http://robotservices.org/)  
[RSNPユニットの仕様](https://ims-lab8073.github.io/RSNPTutorial2020/Specification.html)  

**デモンストレーションを行うには以下のリンクから事前準備を済ましてください**  
[RSNPチュートリアル事前準備](https://ims-lab8073.github.io/RSNPTutorial2020/Setting)

~~~text  
連絡先：  
芝浦工業大学 機械機能工学科 知能機械システム研究室  
〒135-8548 東京都江東区豊洲3-7-5  
機械工学専攻 修士1年 加藤宏一朗 Koichiro Kato
TEL:03-5859-8073
E-mail:md20024@shibaura-it.ac.jp  
~~~  

<div style="page-break-before:always"></div>

## 1 RSNPユニットの動作実行  

プログラムを起動してから，接続する必要があるので注意してください．  

### 1.1 RSNP通信プログラムの実行  
まず，`"RSNPNotifi.jar"`を実行します．  
`RSNPUnit`ディレクトリに移動するため，以下のようにコマンドを入力します．  

```shell
~$ cd ~/RSNPUnit
```

次に，実行するために以下のようにコマンドを入力します．  
```shell
~$ java -jar RSNPNotifi.jar
```
※現状，jdk1.8以下で動作します．jdk10以上では動作しませんのでご注意ください．  

停止するときは，"Ctrl"+"c"キーを入力することで停止します．  

### 1.2 RSNPユニットに接続する
RSNPNotifi.jarに接続するサンプルのPythonプログラムがあります．
新しい接続画面を開いてください．(2.4 RSNPユニットに接続する 参照)

まず，Pythonファイルのある場所に移動します．

```shell
~$ cd ~/RSNPUnit/ConnectorSample
```

その後，Pythonファイルを実行します．

```shell
~$ python Socket_sample.py
```

`Input data and enter`と出てくるので好きな文字を入力してEnterを押します．
```shell
~$ Input data and enter : (なにか文字列を入力)
~$ send data : {"data":[{"ac_id":"1","ac":"robot_state","re_id":"1","re":"RSNPチュートリアル","co":""}]}
```

### 1.3 状態の確認  
ロボットまたはデバイスからRSNPユニットにデータを送信すると，RSNPでサーバに送信されます．
サーバにアクセスすることでWebブラウザ上に状態が反映されているか確認することができます．  

デフォルト設定のままの場合，以下のURLにアクセスすることで確認することができます．  
[http://robo-lab.mydns.jp:8080/RSNPTutorial2020/](http://robo-lab.mydns.jp:8080/RSNPTutorial2020/)

以下のようにブラウザ上で表示されていれば，確認完了です．  
今回は，単にRaspberryPiの稼働状況と，それに接続されたセンサの状態を表示する一例となっています．

"robot_id"=1のロボットで"result"="test_string"を送信した例を下の図に示します．  
![](./images/demoImage.png)  

他にもロボットの画像に差し替えたり，表示するデータの種類も変更して表示情報を変更することができます．  

## 2. RSNPユニットへの通信データ仕様

RSNPユニットからロボットまたはデバイス間のデータのやり取りはSocket,Serial通信で行います．  
送信データは現状，**文字列型データ**です．ただし，以下の5種類のデータで定義づける必要があります．  

- **Action_id**
- **Action名**  
- **Result_id**  
- **Resultデータ**  
- **コメント**  

各データの意味は，次のようになっています．
**Action_id**とは，**Action名**に対する紐づけidです．  
**Action名**とは，ロボットが行った動作名などです．  
**Result_id**とは，**Resultデータ**に対する紐づけidです．  
**Resultデータ**とは，ロボットから得たデータ(変数)などです．  
**コメント**とは，コメント記述を入れたい場合に用います．  
例えば，挨拶を3回，人数カウントを5人としたロボットがあったとします．この場合，データの仕様は次のようになります．  

|     データ名     | データ1  | データ2 |
| :--------------: | :------: | :-----: |
|  **Action_id**   |    1     |    2    |
|   **Action名**   | 挨拶回数 |  人数   |
|  **Result_id**   |    1     |    2    |
| **Resultデータ** |    3     |    5    |
|   **コメント**   |   無し   |  無し   |

ここで，実際のデータ形式は以下のようなjson形式としてます．`{...}`内において，先頭に`「"data":」`があり，その次に配列のカッコ(`[]`)内において，1種類のデータが配列の1つの要素に入ります．ダブルクォーテーション(`"`)で囲んだ仕様名と値をカンマ(`:`)で区切ります．3点(`...`)には，対応するデータ等が入ります．見やすいように改行してありますが，実際は1行でデータ送信してください．これ以外の仕様でのデータを送信するとRSNPユニット側で受信できないのでご注意ください．  

~~~text
{  
  "data":  
  [  
    {  
      "ac_id": ... ,  
      "ac": ... ,  
      "re_id": ... ,  
      "re": ... ,  
      "co": ...  
    },  
    {...},  
    ...  
  ]  
}  
~~~  

データ名は以下の表のように短縮形となっているのでご注意ください．  

|     データ名     |  省略形   |
| :--------------: | :-------: |
|  **Action_id**   | **ac_id** |
|   **Action名**   |  **ac**   |
|  **Result_id**   | **re_id** |
| **Resultデータ** |  **re**   |
|   **コメント**   |  **co**   |

上記のロボットの例の場合は，  
`{"data":[{"ac_id":"1","ac":"挨拶回数","re_id":"1","re":3,"co":""},{"ac_id":"2","ac":"人数","re_id":"2","re":5,"co":""}]}`  
となります(コメントは無しのため，空欄("")となっています)．つまり，最終的にこのデータ形式で**文字列型データ**で送信することになります．  
データが複数種類の場合は，配列の成分が増加し，  
``{"data":[{...},{...},{...},...]}``  
となります．今回は5種類まで対応しています．  