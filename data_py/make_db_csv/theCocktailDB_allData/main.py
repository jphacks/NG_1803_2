# -*- coding: utf-8 -*-
import requests
import json

startNum = 11000
endNum   = 17300
dataNum = endNum - startNum
url = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
dataList_dic = []

for num in range(startNum, startNum+dataNum):
    query = {
    'i': num
    }
    r = requests.get(url, params=query)
    print(num)
    data_json = r.text
    # json形式から辞書型に変換
    data_dic = json.loads(data_json)
    if data_dic['drinks'] != None:
        print(data_dic)
        dataList_dic.append(data_dic)
else:
    print(dataList_dic)
    print('-----JSONファイルとして出力-----')
    fw = open('theCocktailDB_allData.json', 'w')
    # ココ重要！！
    # json.dump関数でファイルに書き込む
    json.dump(dataList_dic, fw)