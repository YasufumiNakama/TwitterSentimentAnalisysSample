# coding:utf-8
import pandas as pd
from natto import MeCab
mc = MeCab()

select = pd.read_csv('./input/keyword.csv', encoding='SHIFT-JIS', header=None)
select = select[0].values.tolist()

tango_retu = []
score_retu = []

# 日本語評価極性辞書（用言編）ver.1.0（2008年12月版）
# ポジの用語は 1 ,ネガの用語は -1 と数値化する
with open("./dictionary/wago.121808.pn.txt", 'r') as f:
    for l in f.readlines():
        l = l.split('\t')
        l[1] = l[1].replace(" ", "").replace('\n', '')
        value = 1 if l[0].split('（')[0] == "ポジ" else -1

        tango_retu.append(l[1])
        score_retu.append(value)

wago_dic = dict(zip(tango_retu, score_retu))

tango_retu = []
score_retu = []

# 日本語評価極性辞書（名詞編）ver.1.0（2008年12月版）
# pの用語は 1 eの用語は 0 ,nの用語は -1 と数値化する
with open("./dictionary/pn.csv.m3.120408.trim", 'r') as f:
    for l in f.readlines():
        l = l.split('\t')

        if l[1] == "p":
            value = 1
        elif l[1] == "e":
            value = 0
        elif l[1] == "n":
            value = -1

        tango_retu.append(l[0])
        score_retu.append(value)

pn_dic = dict(zip(tango_retu, score_retu))

def main():
    for j in range(len(select)):
        # 入力
        df = pd.read_csv('./tweets/' + select[j] + '.csv')

        # スコア算出
        df['score'] = 0

        for i in range(len(df)):
            if df.loc[:, 'text'].isnull()[i]:
                # print(df.loc[i, 'text'])
                score = 0
            else:
                res = mc.parse(df.loc[i, 'text'])
                kaigyou = res.split('\n')
                score = 0

                # 日本語評価極性辞書（用言編）ver.1.0（2008年12月版）
                for tango_list in kaigyou:
                    tab = tango_list.split('\t')
                    if tab[0] in wago_dic:
                        pn_score = wago_dic[tab[0]]
                    else:
                        # pn_score = '辞書に単語がないです'
                        pn_score = 0
                    score += pn_score

                # 日本語評価極性辞書（名詞編）ver.1.0（2008年12月版）
                for tango_list in kaigyou:
                    tab = tango_list.split('\t')
                    if tab[0] in pn_dic:
                        pn_score = pn_dic[tab[0]]
                    else:
                        # pn_score = '辞書に単語がないです'
                        pn_score = 0
                    score += pn_score

                df.loc[i, 'score'] = score

        # 　出力
        df.to_csv('./sentiment_score/' + select[j] + '.csv')
        print('./sentiment_score/' + select[j] + '.csv was created')

if __name__ == "__main__":
    main()