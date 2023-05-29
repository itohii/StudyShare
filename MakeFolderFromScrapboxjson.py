import json
import os
import string
import re

json_open = open('argus-knowledge.json', 'r',encoding = 'utf-8')
json_load = json.load(json_open)

DefaultFolderName = ["ワード","リンク","リスト","本","アイデア"]

for i in DefaultFolderName:
    if not os.path.isdir(i) :
        os.mkdir(i)

print(len(json_load['pages']))

for pagei in range(len(json_load['pages'])):
    # pageデータ取得
    pages = json_load['pages'][pagei]

    # 本文データ取得
    title = pages["title"]
    lines = pages["lines"]
    print(str(pagei) + ":" + title)
    
    # タグデータ取得
    try:
        tagtext = lines[-2]["text"]
    except IndexError:
        title = re.sub(r'[\\|/|:|*|?|"|<|>|\|]', '-', title)
        f = open(DefaultFolderName[0] + "\{}.md".format(title), mode='w',encoding = 'utf-8')
        f.write("# " + title + "\n")

        for i in lines[1:]:
            f.write(i["text"] + "\n")

        f.close()

    if tagtext.find("#") == -1:
        punct = string.punctuation
        title = re.sub(r'[\\|/|:|*|?|"|<|>|\|]', '-', title)
        f = open(DefaultFolderName[0] + "\{}.md".format(title), mode='w',encoding = 'utf-8')
        f.write("# " + title + "\n")

        for i in lines[1:]:
            f.write(i["text"] + "\n")

        f.close()

    else:
        #タグ名からフォルダ作成
        SpaceNone = tagtext.replace(" ",",")
        ShapeNone = SpaceNone.replace("#","")
        FolderNameList = ShapeNone.split(",")

        for i in FolderNameList:
            print(FolderNameList)
        
            if not os.path.isdir(i) :
                os.mkdir(i)

            title = re.sub(r'[\\|/|:|*|?|"|<|>|\|]', '-', title)
            f = open(i + "\{}.md".format(title), mode='w',encoding = 'utf-8')
            f.write("# " + title + "\n")

            for i in lines[1:-3]:
                f.write(i["text"] + "\n")

            f.close()