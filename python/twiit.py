#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YUTO
#
# Created:     23/08/2021
# Copyright:   (c) YUTO 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tweepy
from config import CONFIG
import schedule,time,datetime
import random


CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]
SEARCH_WORD = CONFIG["SEARCH_WORD"]

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
api = tweepy.API(auth)



good_count = 0 #いいねをつけた数 初期値
rand = 60 #ランダムな数字 初期値

now = datetime.datetime.now()
print("起動日時:",now)

def main():

    global good_count
    global rand
    global SEARCH_WORD

    # テキスト最後の行に空白を入れないようにすること
    f = open("./ngword.txt","r") #NGワードを保存しているファイルを読み込む
    ng = [] #NGワード用リストを宣言

    for x in f:
        ng.append(x.rstrip("\n")) #改行コードを除いてリストに入れる
        print(x.rstrip("\n")) #テスト用　リストの中を確認する
    f.close()
    print(len(ng)) #テスト用　リスト要素数を確認

    now=datetime.datetime.now()
    dic = {} #辞書の定義

    search_results = api.search(q=SEARCH_WORD, count=100) #ツイートワード検索 除外されるものも含めて100件検索

    print("検索時:",now) #検索時　時間
    rand = random.randint(20,30)
    time.sleep(rand) #ツイート検索してからどれぐらい待つか
    now=datetime.datetime.now()
    print("スリープ後:",now) #スリープ後　時間

    for result in search_results: #ツイート一件ごとにループ

        NGcheck = False

        text = result.text #ツイートのテキスト部分を変数textに代入
        tweet_id = result.id
        dic.update({id:text}) #id,変数textを紐付けし、辞書dicに追加

        for excpt in ng:
            if excpt in dic[id]: #辞書に登録されたツイート本文中にNGワードがあるか？
                ngword = excpt #検出されたNGワードを変数に保存
                NGcheck = True #リプライ除外を決定

        if NGcheck == True:
            now=datetime.datetime.now()
            print("id{}のツイート".format(result.id)+ ngword +"により除外されました。内容:{}".format(result.text),now)
            pass
        else:
            try:
                api.create_favorite(tweet_id) #ここでいいねする
                now=datetime.datetime.now()
                print("id{}にいいねしています。内容:{}".format(result.id,result.text),now)
                good_count = good_count + 1 #いいねした数をカウント
                rand = random.randint(5,10)
                time.sleep(rand) #いいね一件毎にディレイを設ける

                if good_count == 15: #良いね数最大何個か
                    break

            except Exception as e:
                print(e)

def job():
    global minute
    global good_count
    global rand
    now=datetime.datetime.now()
    main()
    good_count = 0
    rand = random.randint(60,70)
    print("いいねが完了しました。日時：",now,"次回{}分後".format(rand))


minute=rand
schedule.every(minute).minutes.do(job) #何分おきに起動するか


while True:
    schedule.run_pending()
    time.sleep(1)
