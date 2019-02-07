# TwitterSentimentAnalisysSample
## 概要  
Twitterからツイートを取得して感情分析を行うプログラムのサンプル 
## ケーススタディ  
今回はTwitterで企業に対する感情分析を行うことで投資の材料とする  
## 結果
実行結果は以下の順序で確認できます
1. GetTweetsToCSV.ipynb
2. SentimentScore.ipynb
3. SentimentRank.ipynb
## 使い方
### 動作要件
Python3.6での動作を確認しました  
例外処理などは記述されておりませんので悪しからず  
また以下のライブラリをインストールしていない場合はインストールしておく必要があります  
- requests_oauthlib
~~~
$ pip install requests requests_oauthlib
~~~
- natto-py
~~~
$ pip install natto-py
~~~
### API Key
Twitterからデータを取得するためには「Twitter Developer」から「API Key」を取得する必要があります  
個人で取得した「API Key」を公開することはできませんのでコード中では伏せてあります  
そのためコードを実行するには[Twitter Developer](https://developer.twitter.com/)から「API Key」を取得してください  
### 動作手順
1. ./input/keyword.csv  
検索をかけたいキーワードをcsvファイルで用意してください 

2. GetTweetsToCSV.py  
「API Key」を入力する箇所があるので取得した「API Key」に書き換えてください  
以下のコードを実行すると過去7日間まで遡って最大100件のツイートが取得されtweetsディレクトリ下にCSVファイルで保存されます  
~~~
$ python GetTweetsToCSV.py
~~~
3. SentimentScore.py  
以下のコードを実行すると各ツイートに対するSentimentScoreが計算されsentiment_scoreディレクトリ下にCSVファイルで保存されます 
~~~
$ python SentimentScore.py
~~~
4. SentimentRank.py  
以下のコードを実行するとキーワードごとにツイートあたりのスコアが計算され降順でソートされsentiment_rankディレクトリ下にCSVファイルで保存されます 
~~~
$ python SentimentRank.py
~~~
