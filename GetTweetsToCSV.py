# coding:utf-8
import pandas as pd
from requests_oauthlib import OAuth1Session
import json

select = pd.read_csv('./input/keyword.csv', encoding='SHIFT-JIS', header=None)
select = select[0].values.tolist()

URL = 'https://api.twitter.com/1.1/search/tweets.json'

KEYS = {  # 自分のアカウントで入手したキーを下記に記載
    'consumer_key': '**********',
    'consumer_secret': '**********',
    'access_token': '**********',
    'access_secret': '**********',
}


def get_tweets(search_word, count=100):
    if not search_word:  # 検索文字が無い場合は処理を中断
        print ("Plz input 'search_word'")
        return

    twitter = OAuth1Session(
        KEYS['consumer_key'],
        KEYS['consumer_secret'],
        KEYS['access_token'],
        KEYS['access_secret'])
    params = {'q': search_word, 'count': count}

    req = twitter.get(URL, params=params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        metadata = timeline['search_metadata']
        statuses = timeline['statuses']
        return {
            'result': True,
            'metadata': metadata,
            'statuses': statuses, }
    else:
        print ("Error: %d" % req.status_code)
        return {'result': False, 'status_code': req.status_code}

def main():
    # 過去7日間のツイートを最大100件まで取得してCSVに保存
    for i in range(len(select)):
        res = get_tweets(search_word=select[i], count=100)
        df = pd.DataFrame()

        for j in range(len(res['statuses'])):
            if res['result'] == True:
                df.loc[j, 'keyword'] = select[i]
                df.loc[j, 'date'] = res['statuses'][j]['created_at']
                df.loc[j, 'text'] = res['statuses'][j]['text'].replace('\n', '')

        df.to_csv('./tweets/' + select[i] + '.csv')
        print('./tweets/' + select[i] + '.csv of length ' + str(len(df)) + ' was created')

if __name__ == "__main__":
    main()