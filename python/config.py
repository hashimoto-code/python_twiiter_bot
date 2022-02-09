#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YUTO
#
# Created:     25/08/2021
# Copyright:   (c) YUTO 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# テキスト最後の行に空白を入れないようにすること
f = open("./config.txt","r") #ユーザー情報を保存しているファイルを読み込む
user = [] #ユーザー情報用リストを宣言

for x in f:
    user.append(x.rstrip("\n")) #改行コードを除いてリストに入れる
    print(x.rstrip("\n")) #テスト用　リストの中を確認する
f.close()
print(len(user)) #テスト用　リスト要素数を確認


dic = {} #辞書の定義

CONFIG = {
    "CONSUMER_KEY":user[0],
    "CONSUMER_SECRET":user[1],
    "ACCESS_TOKEN":user[2],
    "ACCESS_SECRET":user[3]}



