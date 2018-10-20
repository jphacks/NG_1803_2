# -*- coding: utf-8 -*-
import requests
import csv
import json
from time import sleep
#import make_db_csv

#全ての言語のデータを格納
#あとでmake_db_csvになげる
all_lang_list = []


# for i in csv.DictReader(f):
#     print(i)

# f.close()
##########################################
# お金かかるので注意
##########################################


########################################################################

#オリジナルから成形されたjaのjson,csvを作る

########################################################################

# オリジナルJSON ファイルの読み込み
f = open('original_data/suntoryCocktailRecipe_allData_20181010.json', 'r')
json_dict = json.load(f)
# print(json_dict[0])
# print(len(json_dict))

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
        "cocktail_or_not": 1,
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

#日本語追加
all_lang_list += [format_data_list]

print('-----JSONファイルとして出力-----')
fw = open('format_data/suntoryCocktailRecipe_formatData_ja.json', 'w')
# ココ重要！！
# json.dump関数でファイルに書き込む
json.dump(format_data_list, fw, ensure_ascii=False)

print('-----CSVファイルとして出力-----')
with open('format_data/suntoryCocktailRecipe_formatData_ja.csv', 'w', newline='', encoding='utf_8_sig') as f:
    # dialectの登録
    csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
    # DictWriter作成
    writer = csv.DictWriter(f, fieldnames=format_data_list[0].keys(), dialect='dialect01')
    # CSVへの書き込み
    writer.writeheader()
    for format_data_l in format_data_list:
        writer.writerow(format_data_l)

########################################################################

#formatされた日本語jsonからenとzhへ翻訳し、ja,en,zhをすべて格納したdictを作る

########################################################################

# JSON ファイルの読み込み
# f = open('format_data/suntoryCocktailRecipe_formatData_ja.json', 'r')
# json_dict = json.load(f)
# f.close()
pre_language_data_list = []
post_language_data_list = []



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
    fww = open(common_file_name + '.json', 'w', encoding='UTF-8')
    # ココ重要！！
    # json.dump関数でファイルに書き込む
    json.dump(json_data, fww, ensure_ascii=False)
    fww.close()


# 出力用関数_csv：沢山要素があってカラムをつけるとき
def output_csv(common_file_name, json_data):
    print('-----CSVファイルとして出力-----')
    with open(common_file_name + '.csv', 'w', newline='', encoding='utf_8_sig') as ff:
        # dialectの登録
        csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
        # DictWriter作成
        writer2 = csv.DictWriter(ff, fieldnames=json_data[0].keys(), dialect='dialect01')
        # CSVへの書き込み
        writer2.writeheader()
        for json_data in json_data:
            writer2.writerow(json_data)
    # # csv確認用
    # print(open('translation_data/suntoryCocktailRecipe_translationData_' + post_language + '.csv', 'r').read())


# 出力用関数_csv：要素がきれいな配列のとき
def output_csv_simple(common_file_name, json_data):
    print('-----CSVファイルとして出力-----')
    with open(common_file_name + '.csv', 'w', newline='', encoding='utf_8_sig') as ff:
        # dialectの登録
        csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
        # # DictWriter作成
        writer = csv.DictWriter(ff, fieldnames=json_data.keys(), dialect='dialect01')
        # # CSVへの書き込み
        writer.writeheader()
        # for json_data in json_data:
        writer.writerow(json_data)
    # # csv確認用
    # print(open('translation_data/suntoryCocktailRecipe_translationData_' + post_language + '.csv', 'r').read())


######################################
# 翻訳方法の設定
######################################
# 無料1
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


def translate_data(all_lang_list, post_language):
    # 翻訳した全データ
    translation_data_list = []

    # 翻訳のデータ保存用
    # pre_language_data_list = []     # 翻訳の辞書がまだないとき
    # post_language_data_list = []    # 翻訳の辞書がまだないとき
    ft = open('translation_data_list/suntoryCocktailRecipe_translationDatList_ja_en_201810131020.json', 'r',
            encoding='utf_8_sig')
    language_data_list_dict = json.load(ft)
    pre_language_data_list = list(language_data_list_dict.keys())
    print(pre_language_data_list)
    post_language_data_list = list(language_data_list_dict.values())
    print(post_language_data_list)
    ft.close()
    ##############################################
    # 入力した情報を翻訳して出力する
    for j in range(len(json_dict)):
        # for i in range(7):
        data = json_dict[j]

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

    all_lang_list += [translation_data_list]

    sleep(2)

    # データベースの出力
    name = 'translation_data/suntoryCocktailRecipe_translationData_' + post_language
    output_json(name, translation_data_list)
    output_csv(name, translation_data_list)
    return all_lang_list


json_dict = format_data_list

# 言語設定
pre_language = 'ja'
#post_language = 'en'
# post_language = 'en'

for lang in ['en', 'zh']:
    post_language = lang
    all_lang_list = translate_data(all_lang_list, post_language=post_language)


id_dict = {
    "Drink": 0,
    "DrinkCompornent": 0,
    "Compornent": 0,
    "CompornentDoc": 0,
    "DrinkName": 0,
    "DrinkDoc": 0,
    "DrinkTechnique": 0,
    "DrinkTechniqueDoc": 0,
    "DrinkTaste": 0,
    "DrinkTasteDoc": 0,
    "Grass": 0,
    "GrassDoc": 0,
    "Category": 0,
    "CategoryDoc": 0,
    "Source": 0,
    "Base": 0,
    "BaseDoc": 0
}

def push_in(table, table_name, **keyword_arguments):
    global id_dict
    # Drink_idだけ先に+1しておくので除外
    if (table_name == "Drink"):
        pass
    else:
        id_dict[table_name] += 1
    line = {"id": id_dict[table_name]}
    line.update(keyword_arguments)

    table += [line]


    #

    # drink = {
    # }
    # drinkcompornent = {}
    # drinkcompornent = {}
    # compornent = {}
    # compornentdoc = {}
    # drinkName = {}
    # drinkDoc = {}
    # drinktechniques = {}
    # drinkTaste = {}
    # drinktastedoc = {}
    # grass = {}
    # grassdoc = {}
    # category = {}
    # categorydoc = {}
    # source = {}
    # base = {}
    # baseDoc = {}


def make_db_csv(all_lang_list):
    Drink = []
    DrinkCompornent = []
    DrinkCompornentDoc = []
    Compornent = []
    CompornentDoc = []
    DrinkName = []
    DrinkDoc = []
    DrinkTechnique = []
    DrinkTechniqueDoc = []
    DrinkTaste = []
    DrinkTasteDoc = []
    Grass = []
    GrassDoc = []
    Category = []
    CategoryDoc = []
    Source = []
    Base = []
    BaseDoc = []

    # 日本語リストの要素数ベースで回す
    l = len(all_lang_list[0])
    # JA = 0
    # EN = 1
    # ZH = 2
    ja_lines = all_lang_list[0]
    en_lines = all_lang_list[1]
    zh_lines = all_lang_list[2]

    ingredients_db = {}
    compornent_id = 0

    taste_db = {}
    drink_taste_id = 0

    glass_db = {}
    glass_id = 0

    category_db = {}
    category_id = 0

    base_db = {}
    base_id = 0

    method_category_db = {}
    drink_technique_id = 0

    for i in range(l):
        ja_line = ja_lines[i]
        en_line = en_lines[i]
        zh_line = zh_lines[i]

        # DrinkName#

        ##drink_id先に1足す
        id_dict["Drink"] += 1

        drink_names = [ja_line["drink_name"], en_line["drink_name"], zh_line["drink_name"]]
        priority = ja_line["priority"]
        for lang in range(3):
            push_in(DrinkName, "DrinkName", drink_id=id_dict["Drink"], language=lang, name=drink_names[lang], primary=priority)

        # DrinkDoc#

        # for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="description"]))
        descriptions = [list(ja_line.values())[18], list(en_line.values())[18], list(zh_line.values())[18]]
        # for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="method_detail"]))
        method_details = [ja_line["method_detail"], en_line["method_detail"], zh_line["method_detail"]]
        ##ja_method_detail = ...
        # for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="color"]))
        colors = [ja_line["color"], en_line["color"], zh_line["color"]]
        places = [ja_line["place"], en_line["place"], zh_line["place"]]
        companies = [ja_line["company"], en_line["company"], zh_line["company"]]

        for lang in range(3):
            push_in(Drink, "Drink", drink_id=id_dict["Drink"], language=lang, description=descriptions[lang],
                    recipe=method_details[lang], color=colors[lang], location=places[lang], company=companies[lang])

        # Drink#1

        alcohol_percentage = ja_line["alcohol_percentage"]
        max_degree = 0
        min_degree = 0
        if ("強" in alcohol_percentage):
            max_degree = 40
            min_degree = 25
        elif ("普通" in alcohol_percentage):
            max_degree = 25
            min_degree = 8
        elif ("弱" in alcohol_percentage):
            max_degree = 8
            min_degree = 1

        image_url = ja_line["image"]

        # DrinkCompornent#
        # DrinkCompornentDoc#
        # Compornent#
        # CompornentDoc#

        push_in(Compornent,"Compornent", min_degree=min_degree, max_degree=max_degree, shop_url="", image_url=image_url)

        ingredients = [[ja_line["ingredient1"],
            ja_line["ingredient2"],
            ja_line["ingredient3"],
            ja_line["ingredient4"],
            ja_line["ingredient5"],
            ja_line["ingredient6"],
            ja_line["ingredient7"],
            ja_line["ingredient8"],
            ja_line["ingredient9"],
            ja_line["ingredient10"]
        ],[en_line["ingredient1"],
            en_line["ingredient2"],
            en_line["ingredient3"],
            en_line["ingredient4"],
            en_line["ingredient5"],
            en_line["ingredient6"],
            en_line["ingredient7"],
            en_line["ingredient8"],
            en_line["ingredient9"],
            en_line["ingredient10"]
        ],[zh_line["ingredient1"],
            zh_line["ingredient2"],
            zh_line["ingredient3"],
            zh_line["ingredient4"],
            zh_line["ingredient5"],
            zh_line["ingredient6"],
            zh_line["ingredient7"],
            zh_line["ingredient8"],
            zh_line["ingredient9"],
            zh_line["ingredient10"],
            zh_line["ingredient1"]]
        ]

        amount_numbers = [[ja_line["measure1"],
                           ja_line["measure2"],
                           ja_line["measure3"],
                           ja_line["measure4"],
                           ja_line["measure5"],
                           ja_line["measure6"],
                           ja_line["measure7"],
                           ja_line["measure8"],
                           ja_line["measure9"],
                           ja_line["measure10"]
                           ],
                          [en_line["measure1"],
                           en_line["measure2"],
                           en_line["measure3"],
                           en_line["measure4"],
                           en_line["measure5"],
                           en_line["measure6"],
                           en_line["measure7"],
                           en_line["measure8"],
                           en_line["measure9"],
                           en_line["measure10"]
                           ],
                          [zh_line["measure1"],
                           zh_line["measure2"],
                           zh_line["measure3"],
                           zh_line["measure4"],
                           zh_line["measure5"],
                           zh_line["measure6"],
                           zh_line["measure7"],
                           zh_line["measure8"],
                           zh_line["measure9"],
                           zh_line["measure10"],
                           zh_line["measure1"]]
                          ]

        for j in range(1, 11):
            if not (exec("(ja_line['ingredient{}'])".format(j))):
                ingredients = [ingredients[0][:j - 1], ingredients[1][:j - 1], ingredients[2][j - 1]]
                amount_numbers = [amount_numbers[0][:j - 1], amount_numbers[1][:j - 1], amount_numbers[2][:j - 1]]
                break

        for num, ingredient in enumerate(ingredients[0]):
            if not (ingredient in list(ingredients_db.keys())):
                compornent_id += 1
                ingredients_db[ingredient] = compornent_id

            for lang in range(3):
                push_in(CompornentDoc, "CompornentDoc", compornent_id=ingredients_db[ingredient], language=lang,
                        name=ingredients[lang][num], description="")
            if (type(amount_numbers[0][num]) == str):
                push_in(DrinkCompornent, "DrinkCompornent", drink_id=id_dict["Drink"], compornent_id=compornent_id, amount_number=0)
                for lang in range(3):
                    push_in(DrinkCompornentDoc, "DrinkCompornentDoc", drink_compornent_id=id_dict["DrinkCompornent"], language=lang,
                            amount_string=amount_numbers[lang][num])
            else:
                #チェック
                push_in(DrinkCompornent, "DrinkCompornent", drink_id=id_dict["Drink"], compornent_id=compornent_id,
                        amount_number=amount_numbers[0][num])

        # DrinkTaste#
        # DrinkTasteDoc#

        # for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="taste"]))
        tastes = [ja_line["taste"], en_line["taste"], zh_line["taste"]]
        if not (tastes[0] in list(taste_db.keys())):
            drink_taste_id += 1
            taste_db[tastes[0]] = drink_taste_id
            push_in(DrinkTaste, "DrinkTaste")
        for lang in range(3):
            push_in(DrinkTasteDoc, "DrinkTasteDoc" , drink_taste_id=drink_taste_id, language=lang, taste=tastes[lang])

        # GrassDoc#
        # Grass#

        glasses = [ja_line["glass"], en_line["glass"], zh_line["glass"]]
        cocktailTypes = [ja_line["cocktailType"], en_line["cocktailType"], zh_line["cocktailType"]]

        glass = glasses[0]
        if (
                glass == "ロックグラス" or glass == "タンブラー" or glass == "コリンズグラス" or glass == "ワイングラス" or glass == "ゴブレット" or glass == "ホットグラス" or glass == "ピルスナー"):
            total_amount = 120
        elif (glass == "カクテルグラス" or glass == "ソーサー型シャンパングラス" or glass == "フルート型シャンパングラス" or glass == "サワーグラス"):
            total_amount = 60
        elif (glass == "リキュールグラス" or glass == "ショットグラス"):
            total_amount = 30
        else:
            total_amount = 0

        if not (glasses[0] in list(glass_db.keys())):
            glass_id += 1
            glass_db[glasses[0]] = glass_id
            push_in(Grass, "Grass", total_amount=total_amount)
        for lang in range(3):
            push_in(GrassDoc, "GrassDoc", grass_id=glass_db[glasses[0]], language=lang, name=glasses[lang],
                    grass_type=cocktailTypes[lang])

        # Category
        # CategoryDoc

        view_type = ja_line["cocktail_or_not"]
        categories = [ja_line["category"], en_line["category"], zh_line["category"]]
        if not (categories[0] in list(category_db.keys())):
            category_id += 1
            category_db[categories[0]] = category_id
            push_in(Category, "Category", view_type=view_type)
        for lang in range(3):
            push_in(CategoryDoc, "CategoryDoc", category_id=category_db[categories[0]], language=lang, name=categories[lang])

        # Source

        reference_url = ja_line["reference_url"]
        source = ja_line["source"]
        push_in(Source, "Source", name=source, url=reference_url)

        # Base
        # BaseDoc

        base = [ja_line["base"], en_line["base"], zh_line["base"]]
        if not (base[0] in list(base_db.keys())):
            base_id += 1
            base_db[base[0]] = base_id
            push_in(Base, "Base", image_url=image_url)
        for lang in range(3):
            push_in(BaseDoc, "BaseDoc", base_id=base_db[base[0]], language=lang, name=base[lang], description="")

        # DrinkTechnique
        # DrinkTechniqueDoc

        method_categories = [ja_line["method_category"], en_line["method_category"], zh_line["method_category"]]
        if not (method_categories[0] in (method_category_db.keys())):
            drink_technique_id += 1
            method_category_db[method_categories[0]] = drink_technique_id
            push_in(DrinkTechnique, "DrinkTechnique")
        for lang in range(3):
            push_in(DrinkTechniqueDoc, "DrinkTechniqueDoc", drink_technique_id=method_category_db[method_categories[0]], language=lang,
                    name=method_categories[lang], description="")

        # Drink#2

        push_in(Drink, "Drink", drink_taste_id=drink_taste_id, min_degree=min_degree, max_degree=max_degree,
                image_url=image_url, shop_url="", grass_id=glass_db[glasses[0]], category_id=category_db[categories[0]],
                source_id=id_dict["Source"], base_id=base_db[base[0]],
                drink_technique_id=method_category_db[method_categories[0]])

    result = {
        "Drink": Drink,
        "DrinkCompornent": DrinkCompornent,
        "Compornent": Compornent,
        "CompornentDoc": CompornentDoc,
        "DrinkName": DrinkName,
        "DrinkDoc": DrinkDoc,
        "DrinkTechnique": DrinkTechnique,
        "DrinkTechniqueDoc": DrinkTechniqueDoc,
        "DrinkTaste": DrinkTaste,
        "DrinkTasteDoc": DrinkTasteDoc,
        "Grass": Grass,
        "GrassDoc": GrassDoc,
        "Category": Category,
        "CategoryDoc": CategoryDoc,
        "Source": Source,
        "Base": Base,
        "BaseDoc": BaseDoc
    }

    print('-----CSVファイルとして出力-----')
    for key, value in result.items():
        with open('db_csv/{}.csv'.format(key), 'w', newline='', encoding='utf_8_sig') as f:
            csvwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            try:
                csvwriter.writerow(list(value[0].keys()))
                print("ok")
            except:
                print(key)
                print(list(result.values()))
            for v in value:
                csvwriter.writerow(list(v.values()))




#db用csv作成
make_db_csv(all_lang_list)