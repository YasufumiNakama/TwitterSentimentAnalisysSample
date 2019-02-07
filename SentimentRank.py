# coding:utf-8
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

select = pd.read_csv('./input/keyword.csv', encoding='SHIFT-JIS', header=None)
select = select[0].values.tolist()

def main():
    av_score = []
    n_tweets = []

    for j in range(len(select)):
        # 入力
        df = pd.read_csv('./sentiment_score/' + select[j] + '.csv')
        # ツイートあたりのスコア（合計スコア/ツイート数）
        if len(df) == 0:
            av_score.append(0)
        else:
            av_score.append(df['score'].sum() / len(df))
        # ツイート数
        n_tweets.append(len(df))

    # 出力
    rank = pd.DataFrame()
    rank['stock'] = select
    rank['score'] = av_score
    rank['n_tweets'] = n_tweets
    rank = rank.sort_values('score', ascending=False)
    rank.to_csv('./sentiment_rank/rank.csv', encoding='SHIFT_JIS', index=False)
    print('./sentiment_rank/rank.csv was created')

    # ツイート数が10以上のTOP10
    print('TOP 5 Scores Over 10 Tweets')
    print(rank.loc[rank['n_tweets'] >= 10].head(10))

if __name__ == "__main__":
    main()