# -*- coding: utf-8 -*-
import requests
import csv
import json
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse

# JSON ファイルの読み込み
f = open('format_data/suntoryCocktailRecipe_formatData_ja.json', 'r', encoding='UTF-8')
json_dict = json.load(f)
f.close()
print(json_dict)

# 翻訳した全データ
translation_data_list = []

# 言語設定
pre_language = 'ja'
post_language = 'zh'

# 翻訳のデータ入力と保存用
# pre_language_data_list = []     # 翻訳の辞書がまだないとき
# post_language_data_list = []    # 翻訳の辞書がまだないとき
f = open('translation_data_list/suntoryCocktailRecipe_translationDatList_ja_zh_201810131154.json', 'r',
         encoding='utf_8_sig')
language_data_list_dict = json.load(f)
pre_language_data_list = list(language_data_list_dict.keys())
print(pre_language_data_list)
post_language_data_list = list(language_data_list_dict.values())
print(post_language_data_list)
f.close()

# PythonでGoogle Language APIを使うときに、’がデコードされなくて困った
def apostrophe_decode(text):
    return text.replace('&#39;', '\'')


def my_index(x, l, default=-1):
    if x in l:
        return l.index(x)
    else:
        return default


########################################
# 出力関係
########################################
# 出力用関数json
def output_json(common_file_name, json_data):
    print('-----JSONファイルとして出力-----')
    fw = open(common_file_name + '.json', 'w', encoding='UTF-8')
    # ココ重要！！
    # json.dump関数でファイルに書き込む
    json.dump(json_data, fw, ensure_ascii=False)
    fw.close()


# 出力用関数_csv：沢山要素があってカラムをつけるとき
def output_csv(common_file_name, json_data):
    print('-----CSVファイルとして出力-----')
    with open(common_file_name + '.csv', 'w', newline='', encoding='utf_8_sig') as f:
        # dialectの登録
        csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
        # DictWriter作成
        writer = csv.DictWriter(f, fieldnames=json_data[0].keys(), dialect='dialect01')
        # CSVへの書き込み
        writer.writeheader()
        for json_data in json_data:
            writer.writerow(json_data)
    # # csv確認用
    # print(open('translation_data/suntoryCocktailRecipe_translationData_' + post_language + '.csv', 'r').read())


# 出力用関数_csv：要素がきれいな配列のとき
def output_csv_simple(common_file_name, json_data):
    print('-----CSVファイルとして出力-----')
    with open(common_file_name + '.csv', 'w', newline='', encoding='utf_8_sig') as f:
        # dialectの登録
        csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
        # # DictWriter作成
        writer = csv.DictWriter(f, fieldnames=json_data.keys(), dialect='dialect01')
        # # CSVへの書き込み
        writer.writeheader()
        # for json_data in json_data:
        writer.writerow(json_data)
    # # csv確認用
    # print(open('translation_data/suntoryCocktailRecipe_translationData_' + post_language + '.csv', 'r').read())


# 無料で翻訳可能
def how_to_translate(pre_text):
    url = "https://script.google.com/macros/s/AKfycbwG1qRfk6TqJoAieH8o2S8DYDFb1zjZ1mYi2vAEV8QoavkAVWc/exec"

    query = {
        'text': pre_text,
        'source': pre_language,  # そのページにレシピがないとなったらやめる
        'target': post_language,  # そのページに表示する数だから好きに設定できる
    }
    flag = 0
    while True:
        r = requests.get(url, params=query)
        if r.status_code == 200:  # 接続が上手くいった
            print("翻訳中...")
            # 接続が上手くいった
            post_text = r.text
            sleep(0.001)
            flag += 1
            break
        else:
            # APIの処理が止まるので、遅らせる
            sleep(1)
            if flag > 1000:
                post_text = "error"
                print("######################################")
                print("error")
                print("######################################")
                break
    return post_text


#########################################################################
# 翻訳関数本体
def translate(pre_text):
    if pre_text:
        # print(pre_text)
        language_list_i = my_index(pre_text, pre_language_data_list)
        # print(language_list_i)
        if language_list_i >= 0:
            post_text = post_language_data_list[language_list_i]
            post_text = apostrophe_decode(post_text)
            post_language_data_list[language_list_i] = post_text
        else:
            post_text = how_to_translate(pre_text)

            # アポストロフィーのデコード
            post_text = apostrophe_decode(post_text)
            print(post_text)

            # 配列に追加
            pre_language_data_list.append(pre_text)
            post_language_data_list.append(post_text)

            # 翻訳データの出力
            language_list_dict = dict(zip(pre_language_data_list, post_language_data_list))
            print(language_list_dict)
            output_name = 'translation_data_list/suntoryCocktailRecipe_translationDatList_' + pre_language + '_' + post_language
            output_json(output_name, language_list_dict)
            # output_csv_simple(output_name, language_list_dict)
    else:
        post_text = ''

    return post_text


##############################################
# 入力した情報を翻訳して出力する
for i in range(len(json_dict)):
    # for i in range(7):
    data = json_dict[i]

    translation_data = {
        # "object_id": data["object_id"],
        "drink_id": data["drink_id"],
        "language": post_language,
        "priority": data["priority"],
        "drink_name": translate(data["drink_name"]),
        "alcoholic": data["alcoholic"],
        "cocktail_or_not": data["cocktail_or_not"],
        "category": translate(data["category"]),
        "base": translate(data["base"]),
        "place": translate(data["place"]),
        "company": translate(data["company"]),
        "cocktailType": translate(data["cocktailType"]),
        "glass": translate(data["glass"]),
        "taste": translate(data["taste"]),
        "color": translate(data["color"]),
        "alcohol_percentage": translate(data["alcohol_percentage"]),
        "method_category": translate(data["method_category"]),
        "method_detail": translate(data["method_detail"]),
        # "description": translate(data["description"]),
        "image": data["image"],
        "ingredient1": translate(data["ingredient1"]),
        "ingredient2": translate(data["ingredient2"]),
        "ingredient3": translate(data["ingredient3"]),
        "ingredient4": translate(data["ingredient4"]),
        "ingredient5": translate(data["ingredient5"]),
        "ingredient6": translate(data["ingredient6"]),
        "ingredient7": translate(data["ingredient7"]),
        "ingredient8": translate(data["ingredient8"]),
        "ingredient9": translate(data["ingredient9"]),
        "ingredient10": translate(data["ingredient10"]),
        "measure1": translate(data["measure1"]),
        "measure2": translate(data["measure2"]),
        "measure3": translate(data["measure3"]),
        "measure4": translate(data["measure4"]),
        "measure5": translate(data["measure5"]),
        "measure6": translate(data["measure6"]),
        "measure7": translate(data["measure7"]),
        "measure8": translate(data["measure8"]),
        "measure9": translate(data["measure9"]),
        "measure10": translate(data["measure10"]),
        "source": translate(data["source"]),
        "reference_url": data["reference_url"],
        "date_modified": data["date_modified"]
    }
    print(translation_data)
    # 配列に追加
    translation_data_list.append(translation_data)
    # print(translation_data_list)

sleep(2)

# データベースの出力
name = 'translation_data/suntoryCocktailRecipe_translationData_' + post_language
output_json(name, translation_data_list)
output_csv(name, translation_data_list)
