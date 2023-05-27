# jsonファイル読み込み
import json
import os

json_open = open('argus-knowledge.json', 'r',encoding = 'utf-8')
json_load = json.load(json_open)

# pageデータ取得
c1 = json_load['pages'][0]

# 本文データ取得
c2 = c1["title"]

c3 = c1["lines"]

f = open("ワード\{}.md".format(c2), mode='w',encoding = 'utf-8')
f.write("# " + c2 + "\n")

for i in c3[1:-3]:
    f.write(i["text"] + "\n")

f.close()

# # タグデータ取得
# c3 = c2[-2]["text"]
# print(c3)

# #タグ名からフォルダ作成
# SpaceNone = c3.replace(" ",",")
# ShapeNone = SpaceNone.replace("#","")
# FolderNameList = ShapeNone.split(",")
# print(FolderNameList)

# for i in range(len(json_load['pages'])):
    # # pageデータ取得
    # c1 = json_load['pages'][i]

    # # 本文データ取得
    # c2 = c1["title"]
    # print(c2)

    # # タグデータ取得
    # c3 = c2[-2]["text"]
    # # print(c3)

    # #タグ名からフォルダ作成
    # SpaceNone = c3.replace(" ",",")
    # ShapeNone = SpaceNone.replace("#","")
    # FolderNameList = ShapeNone.split(",")
    # print(FolderNameList)