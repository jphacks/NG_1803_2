# coding:utf-8

import json
import csv
from time import sleep

# JSON ファイルの読み込み
f = open('original_data/suntoryCocktailRecipe_allData_20181010.json', 'r')
json_dict = json.load(f)
print(json_dict[0])
print(len(json_dict))

format_data_list = []

for i in range(len(json_dict)):
    # i番目のデータを取得
    data = json_dict[i]

    # howToが配列なので直す：単純に連結するだけ、必要なら改行入れてもよい
    str_howTo = ''
    for item in range(len(data["howTo"])):
        str_howTo += data["howTo"][item]

    # ingredientの配列に空白文字を入れる
    len_ingredient = len(data["ingredient"])
    if len_ingredient < 10:
        for item in range(10 - len_ingredient):
            data["ingredient"].append('')

    # measureの配列に空白文字を入れる
    len_measure = len(data["measure"])
    if len_measure < 10:
        for item in range(10 - len_measure):
            data["measure"].append('')

    format_data = {
        "object_id": data["cocktailId"],
        "drink_id": data["cocktailId"],
        "language": "ja",
        "priority": True,
        "drink_name": data["name_JP"],
        "alcoholic": "Alcohol",
        "cocktail_or_not": True,    # 0,1（0原液、1カクテル：これはview_typeに対応する）にすべき
        "category": "カクテル",
        "base": data["base"],
        "place": '',
        "company": '',
        "cocktailType": data["cocktailType"],
        "glass": data["glass"],
        "taste": data["taste"],
        "color": data["color"],
        "alcohol_percentage": data["alcoholPercentage"],
        "method_category": data["preparation"],
        "method_detail": str_howTo,
        "description": data["onePoint"],
        "image": data["img"],
        "ingredient1": data["ingredient"][0],
        "ingredient2": data["ingredient"][1],
        "ingredient3": data["ingredient"][2],
        "ingredient4": data["ingredient"][3],
        "ingredient5": data["ingredient"][4],
        "ingredient6": data["ingredient"][5],
        "ingredient7": data["ingredient"][6],
        "ingredient8": data["ingredient"][7],
        "ingredient9": data["ingredient"][8],
        "ingredient10": data["ingredient"][9],
        "measure1": data["measure"][0],
        "measure2": data["measure"][1],
        "measure3": data["measure"][2],
        "measure4": data["measure"][3],
        "measure5": data["measure"][4],
        "measure6": data["measure"][5],
        "measure7": data["measure"][6],
        "measure8": data["measure"][7],
        "measure9": data["measure"][8],
        "measure10": data["measure"][9],
        "source": "SUNTORYカクテルレシピ検索",
        "reference_url": data["referenceUrl"],
        "date_modified": "2018-10-11 15:06:00"
    }

    # 配列に追加
    format_data_list.append(format_data)
print(format_data_list)


print('-----JSONファイルとして出力-----')
file_name = 'format_data/suntoryCocktailRecipe_formatData_ja.json'
fw = open(file_name, 'w', encoding='UTF-8')
# ココ重要！！
# json.dump関数でファイルに書き込む
json.dump(format_data_list, fw, ensure_ascii=False)
fw.close()


print('-----CSVファイルとして出力-----')
with open('format_data/suntoryCocktailRecipe_formatData_ja.csv', 'w', newline='', encoding='utf_8_sig') as f:
    # dialectの登録
    csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
    # DictWriter作成
    writer = csv.DictWriter(f, fieldnames=format_data_list[0].keys(), dialect='dialect01')
    # CSVへの書き込み
    writer.writeheader()
    for format_data_list in format_data_list:
        writer.writerow(format_data_list)
# csv確認用
# print (open('format_data/suntoryCocktailRecipe_formatData_ja.csv', 'r').read())
