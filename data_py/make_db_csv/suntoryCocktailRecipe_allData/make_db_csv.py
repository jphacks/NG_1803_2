# -*- coding: utf-8 -*-
import csv


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

def push_in(table, **keyword_arguments):
    global id_dict
    #Drink_idだけ先に+1しておくので除外
    if (table == "Drink"):
        pass
    else:
        id_dict[table] += 1
    line = {"id": id_dict[table]}
    line.update(keyword_arguments)
    table += [line]


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

    #日本語リストの要素数ベースで回す
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
        
        #DrinkName#
        
        ##drink_id先に1足す
        id_dict["Drink"] += 1

        drink_names = [ja_line["drink_name"], en_line["drink_name"], zh_line["drink_name"]]
        priority = ja_line["priority"]
        for lang in range(3):
            push_in("Drinkname", drink_id=id_dict["Drink"], language=lang, name=drink_names[lang], primary=priority)
        
        #DrinkDoc#

        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="description"]))
        descriptions = [ja_line["description"], en_line["description"], zh_line["deescription"]]
        ##ja_description = ...
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="method_detail"]))
        method_details = [ja_line["method_detail"], en_line["method_detail"], zh_line["method_detail"]]
        ##ja_method_detail = ...
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="color"]))
        colors = [ja_line["color"], en_line["color"], zh_line["color"]]
        places = [ja_line["place"], en_line["place"], zh_line["place"]]
        companies = [ja_line["company"], en_line["company"], zh_line["company"]]

        for lang in range(3):
            push_in("Drink", drink_id=id_dict["Drink"], language=lang, description=descriptions[lang], recipe=method_details[lang], color=colors[lang], location=places[lang], company=companies[lang])


        #Drink#1

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


        #DrinkCompornent#
        #DrinkCompornent#
        #Compornent#
        #CompornentDoc#

        push_in("Compornent", min_degree=min_degree, max_degree=max_degree, shop_url="", image_url=image_url)

        ingredients = [[
            ja_line["ingredient1"],
            ja_line["ingredient2"],
            ja_line["ingredient3"],
            ja_line["ingredient4"],
            ja_line["ingredient5"],
            ja_line["ingredient6"],
            ja_line["ingredient7"],
            ja_line["ingredient8"],
            ja_line["ingredient9"],
            ja_line["ingredient10"]
            ],[
            en_line["ingredient1"],
            en_line["ingredient2"],
            en_line["ingredient3"],
            en_line["ingredient4"],
            en_line["ingredient5"],
            en_line["ingredient6"],
            en_line["ingredient7"],
            en_line["ingredient8"],
            en_line["ingredient9"],
            en_line["ingredient10"]
            ],[
            zh_line["ingredient1"],
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

        amount_numbers = [[ja_line["mesure1"],
            ja_line["mesure2"],
            ja_line["mesure3"],
            ja_line["mesure4"],
            ja_line["mesure5"],
            ja_line["mesure6"],
            ja_line["mesure7"],
            ja_line["mesure8"],
            ja_line["mesure9"],
            ja_line["mesure10"]
            ],
            [en_line["mesure1"],
            en_line["mesure2"],
            en_line["mesure3"],
            en_line["mesure4"],
            en_line["mesure5"],
            en_line["mesure6"],
            en_line["mesure7"],
            en_line["mesure8"],
            en_line["mesure9"],
            en_line["mesure10"]
            ],
            [zh_line["mesure1"],
            zh_line["mesure2"],
            zh_line["mesure3"],
            zh_line["mesure4"],
            zh_line["mesure5"],
            zh_line["mesure6"],
            zh_line["mesure7"],
            zh_line["mesure8"],
            zh_line["mesure9"],
            zh_line["mesure10"],
            zh_line["mesure1"]]
        ]
        mesure_numbers = []
        for j in range(1, 11):
            if not (exec("(ja_line['ingredient{}'])".format(j))):
                ingredients = [ingredients[0][:j-1], ingredients[1][:j-1], ingredients[2][j-1]]
                amount_numbers = [amount_numbers[0][:j-1], amount_numbers[1][:j-1], amount_numbers[2][:j-1]]
        
        for num, ingredient in enumerate(ingredients[0]):
            if not (ingredient in list(ingredients_db.keys())):
                compornent_id += 1
                ingredients_db[ingredient] = compornent_id

            for lang in range(3):
                push_in("CompornentDoc", compornent_id=ingredients_db[ingredient], language=lang, name=ingredients[lang][num], description="")
            if (type(amount_numbers[0][num]) == str):
                push_in("DrinkCompornent", drink_id=id_dict["Drink"], compornent_id=compornent_id, amount_number=0)
                for lang in range(3):
                    push_in("DrinkCompornentDoc", drink_compornent_id=id_dict["DrinkCompornent"], language=lang, amount_string=amount_numbers[lang][num])
            else:
                push_in("DrinkCompornent", drink_id=id_dict["Drink"], compornent_id=compornent_id, amount_number=amount_numbers[lang][num])


        #DrinkTaste#
        #DrinkTasteDoc#

        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="taste"]))
        tastes = [ja_line["taste"], en_line["taste"], zh_line["taste"]]
        if not (tastes[0] in list(taste_db.keys())):
            drink_taste_id += 1
            taste_db[tastes[0]] = drink_taste_id
            push_in("Drinktaste")
        for lang in range(3):
            push_in("DrinkTasteDoc", drink_taste_id=drink_taste_id, language=lang, taste=tastes[lang])

        #GrassDoc#
        #Grass#

        glasses = [ja_line["glass"], en_line["glass"], zh_line["glass"]]
        cocktailTypes = [ja_line["cocktailType"], en_line["cocktailType"], zh_line["cocktailType"]]

        glass = glasses[0]
        if (glass == "ロックグラス" or glass == "タンブラー" or glass == "コリンズグラス" or glass == "ワイングラス" or glass == "ゴブレット" or glass == "ホットグラス" or glass == "ピルスナー"):
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
            push_in("Grass", total_amount=total_amount)
        for lang in range(3):
            push_in("GrassDoc", grass_id=glass_db[glasses[0]], language=lang, name=glasses[lang], grass_type=cocktailTypes[lang])


        #Category
        #CategoryDoc

        view_type = ja_line["cocktail_or_not"]
        categories = [ja_line["category"], en_line["category"], zh_line["category"]]
        if not (categories[0] in list(category_db.keys())):
            category_id += 1
            category_db[categories[0]] = category_id
            push_in("Category", view_type=view_type)
        for lang in range(3):
            push_in("CategoryDoc", category_id=category_db[categories[0]], language=lang, name=categories[lang])

        #Source

        reference_url = ja_line["reference_url"]
        source = ja_line["source"]
        push_in("Source", name=source, url=reference_url)


        #Base
        #BaseDoc

        base = [ja_line["base"], en_line["base"], zh_line["base"]]
        if not (base[0] in list(base_db.keys())):
            base_id += 1
            base_db[base[0]] = base_id
            push_in("Base", image_url=image_url)
        for lang in range(3):
            push_in("BaseDoc", base_id=base_db[base[0]], language=lang, name=base[lang], description="")


        #DrinkTechnique
        #DrinkTechniqueDoc

        method_categories = [ja_line["method_category"], en_line["method_category"], zh_line["method_category"]]
        if not (method_categories[0] in (method_category_db.keys())):
            drink_technique_id += 1
            method_category_db[method_categories[0]] = drink_technique_id
            push_in("DrinkTechnique")
        for lang in range(3):
            push_in("DrinkTechniqueDoc", drink_technique_id=method_category_db[method_categories[0]], language=lang, name=method_categories[lang], description="")
        
        
        #Drink#2

        push_in("Drink", drink_taste_id=drink_taste_id, min_degree=min_degree, max_degree=max_degree, image_url=image_url, shop_url="", grass_id=glass_db[glasses[0]], category_id=category_db[categories[0]], source_id=id_dict["Source"], base_id=base_db[base[0]], drink_technique_id=method_category_db[method_categories[0]])

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
            # dialectの登録
            csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
            # DictWriter作成
            writer = csv.DictWriter(f, fieldnames=value[0].keys(), dialect='dialect01')
            # CSVへの書き込み
            writer.writeheader()
            for v in value:
                writer.writerow(v)


