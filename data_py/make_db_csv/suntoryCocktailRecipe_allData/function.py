import csv
csv.field_size_limit(1000000000)

# テーブルにふるidを他から参照しやすいように保持
id_dict = {
    "Drink": 0,
    "DrinkCompornent": 0,
    "DrinkCompornentDoc": 0,
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

# 各テーブルのCSV元リスト
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

# 最後テーブルを投げやすいように格納
result = {
    "Drink": Drink,
    "DrinkCompornent": DrinkCompornent,
    "DrinkCompornentDoc": DrinkCompornentDoc,
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


# テーブルにrowを追加する関数
def push_in(table_name, **keyword_arguments):
    global id_dict, result

    # Drink_idだけ便宜上先に+1しておくので除外
    if (table_name == "Drink"):
        pass
    else:
        id_dict[table_name] += 1

    # idはグローバルで管理
    row = {"id": id_dict[table_name]}
    row.update(keyword_arguments)

    result[table_name] += [row]

# def make_name_json(all_lang_list):
#     import json
#     # 日本語リストの要素数ベースで回す
#     l = len(all_lang_list[0])
#     # それぞれの言語のjsonたち
#     ja_lines = all_lang_list[0]
#     en_lines = all_lang_list[1]
#     zh_lines = all_lang_list[2]

#     drink_names = []
#     for i in range(l):
#         # 一行
#         ja_line = ja_lines[i]
#         en_line = en_lines[i]
#         zh_line = zh_lines[i]

#         drink_names += [{"ja":ja_line["drink_name"], "en":en_line["drink_name"], "zh":zh_line["drink_name"]}]

#     print(drink_names)
#     fw = open('test_json/test_drink_name.json', 'w', encoding="utf-8_sig")
#     # ココ重要！！
#     # json.dump関数でファイルに書き込む
#     json.dump(drink_names, fw, ensure_ascii=False)
#     return

def make_change_image_dict(drink_names):
    import re
    import json
    import difflib
    from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
    from simstring.measure.cosine import CosineMeasure
    from simstring.database.dict import DictDatabase
    from simstring.searcher import Searcher

    ff = open('jsons/theCocktailDB_allData_20181010.json', 'r', encoding="utf-8_sig")
    json_data2 = json.load(ff)
    ff.close()

    # 互いに類似度を比較する文字列のリスト
    STR_db = [re.sub(r'[!-/:-@[-`{-~]', " ", d["en"]) for d in drink_names]
    TCD_db ={re.sub(r'[!-/:-@[-`{-~]', " ", d["drinks"][0]["strDrink"]): d["drinks"][0]["strDrinkThumb"] for d in json_data2}
    TCD_name_db = list(TCD_db.keys())
    count = 0
    length = len(STR_db)
    result_dict = {}
    change_image_dict = {}

    
    db = DictDatabase(CharacterNgramFeatureExtractor(2))
    for str1 in STR_db:
        db.add(str1)
    
    for str2 in TCD_name_db:
        result_dict[str2] = {}
        searcher = Searcher(db, CosineMeasure())
        i = 1.0
        # 類似度を計算、0.0~1.0 で結果が返る
        flag = False
        for str1 in STR_db:
            s = difflib.SequenceMatcher(None, str2, str1).ratio()
            if s > 0.75:
                flag = True
                if (str1 in result_dict[str2]):
                    
                    d =  result_dict[str2][str1]
                    #平均更新
                    d = [(d[0]*d[1]+s)/(d[1]+1), d[1]+1]
                    
                    result_dict[str2][str1] = d
                else:
                    
                    result_dict[str2].setdefault(str1, [s ,1])
                    
        
        temp = []
        while i >= 0.65:
            result = searcher.search(str2, i)
            if (len(result)):
                flag = True
                for str1 in result:
                    if (str1 in temp): continue
                    temp += [str1]
                    if (str1 in result_dict[str2]):
                        
                        d =  result_dict[str2][str1]
                        #平均更新
                        d = [(d[0]*d[1]+i)/(d[1]+1), d[1]+1]
                        
                        result_dict[str2][str1] = d
                    else:
                        result_dict[str2].setdefault(str1, [i ,1])
                        
                        
            i -= 0.001
        if (flag):
            
            count += 1
        
    with open("./search_log.txt", "w+", encoding="utf-8_sig") as f:
        real_count = 0
        for str2 in TCD_name_db:
            print("\n", file=f)
            print("\n")
            print(">> "+str2, file=f)
            print(">> "+str2)
            M = 0.0
            name = ""
            for key, value_list in result_dict[str2].items():
                if (M < value_list[0]):
                    name = key
                    M = value_list[0]
            print("  "+name+": "+str(M), file=f)
            if (M != 0):
                if (M >= 0.76):
                    print("  "+name+": "+str(M))
                    print("ok", file=f)
                    print("ok")
                    change_image_dict[name] = TCD_db[str2]
                    real_count += 1
                else:
                    print("  "+name+": "+str(M))
                    print("out", file=f)
                    print("out")
            

        print("\nmatch is {count}/{length} but real_match is {real_count}/{length}".format(count=count, real_count=real_count, length=length), file=f)
        print("\nmatch is {count}/{length} but real_match is {real_count}/{length}".format(count=count, real_count=real_count, length=length))

    exit()
    return change_image_dict

def make_db_csv(all_lang_list):
    # 日本語リストの要素数ベースで回す
    l = len(all_lang_list[0])

    # JA = 0
    # EN = 1
    # ZH = 2

    # 新規出現順にidをふるため、dictで保持
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

    # それぞれの言語のjsonたち
    ja_lines = all_lang_list[0]
    en_lines = all_lang_list[1]
    zh_lines = all_lang_list[2]
    
    drink_names = []
    for i in range(l):
        # 一行
        ja_line = ja_lines[i]
        en_line = en_lines[i]
        zh_line = zh_lines[i]

        drink_names += [{"ja":ja_line["drink_name"], "en":en_line["drink_name"], "zh":zh_line["drink_name"]}]
    
    change_image_dict = make_change_image_dict(drink_names)
    change_image_name_list = list(change_image_dict.keys())

    for i in range(l):
        # 一行
        ja_line = ja_lines[i]
        en_line = en_lines[i]
        zh_line = zh_lines[i]

        ##drink_id先に1足す
        id_dict["Drink"] += 1


        #############
        # DrinkName #
        #############

        drink_names = [ja_line["drink_name"], en_line["drink_name"], zh_line["drink_name"]]
        priority = ja_line["priority"]

        for lang in range(3):
            push_in("DrinkName", drink_id=id_dict["Drink"], language=lang, name=drink_names[lang], primary=priority)


        ############
        # DrinkDoc #
        ############

        descriptions = [list(ja_line.values())[18], list(en_line.values())[18], list(zh_line.values())[18]]
        method_details = [ja_line["method_detail"], en_line["method_detail"], zh_line["method_detail"]]
        colors = [ja_line["color"], en_line["color"], zh_line["color"]]
        places = [ja_line["place"], en_line["place"], zh_line["place"]]
        companies = [ja_line["company"], en_line["company"], zh_line["company"]]

        for lang in range(3):
            push_in("DrinkDoc", drink_id=id_dict["Drink"], language=lang, description=descriptions[lang],
                    recipe=method_details[lang], color=colors[lang], location=places[lang], company=companies[lang])

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

        if not (en_line["drink_name"] in change_image_name_list):
            if (".gif" in ja_line["image"]): image_url = ""
            else: image_url = ja_line["image"]
        else: image_url = change_image_dict[en_line["drink_name"]]

        ######################
        # DrinkCompornent    #
        # DrinkCompornentDoc #
        # Compornent         #
        # CompornentDoc      #
        ######################

        push_in("Compornent", min_degree=min_degree, max_degree=max_degree, shop_url="", image_url=image_url)

        _ingredients = [[ja_line["ingredient1"],
                         ja_line["ingredient2"],
                         ja_line["ingredient3"],
                         ja_line["ingredient4"],
                         ja_line["ingredient5"],
                         ja_line["ingredient6"],
                         ja_line["ingredient7"],
                         ja_line["ingredient8"],
                         ja_line["ingredient9"],
                         ja_line["ingredient10"]
                         ],
                        [en_line["ingredient1"],
                         en_line["ingredient2"],
                         en_line["ingredient3"],
                         en_line["ingredient4"],
                         en_line["ingredient5"],
                         en_line["ingredient6"],
                         en_line["ingredient7"],
                         en_line["ingredient8"],
                         en_line["ingredient9"],
                         en_line["ingredient10"]
                         ],
                        [zh_line["ingredient1"],
                         zh_line["ingredient2"],
                         zh_line["ingredient3"],
                         zh_line["ingredient4"],
                         zh_line["ingredient5"],
                         zh_line["ingredient6"],
                         zh_line["ingredient7"],
                         zh_line["ingredient8"],
                         zh_line["ingredient9"],
                         zh_line["ingredient10"]
                         ]]

        _amount_numbers = [[ja_line["measure1"],
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
                            zh_line["measure10"]
                            ]]

        #構成要素がいくつあるかを調べて空欄を排除
        for j in range(1, 11):
            if (_ingredients[0][j - 1] == ""):
                ingredients = [_ingredients[0][:j - 1], _ingredients[1][:j - 1], _ingredients[2][:j - 1]]
                amount_numbers = [_amount_numbers[0][:j - 1], _amount_numbers[1][:j - 1], _amount_numbers[2][:j - 1]]
                break
        else:
            ingredients = [_ingredients[0], _ingredients[1], _ingredients[2]]
            amount_numbers = [_amount_numbers[0], _amount_numbers[1], _amount_numbers[2]]
            break

        #日本語データをベースに更新作業
        for num, ingredient in enumerate(ingredients[0]):
            #既に存在しているComponentか？
            if not (ingredient in list(ingredients_db.keys())):
                #id割り振り
                compornent_id += 1
                ingredients_db[ingredient] = compornent_id

            #言語分更新
            for lang in range(3):
                push_in("CompornentDoc", compornent_id=ingredients_db[ingredient], language=lang,
                        name=ingredients[lang][num], description="")

            #もしComponentの量がstrなら
            if (type(amount_numbers[0][num]) == str):
                push_in("DrinkCompornent", drink_id=id_dict["Drink"],
                        compornent_id=ingredients_db[ingredient], amount_number=0)
                for lang in range(3):
                    push_in("DrinkCompornentDoc", drink_compornent_id=id_dict["DrinkCompornent"],
                            language=lang,
                            amount_string=amount_numbers[lang][num])
            else:
                push_in("DrinkCompornent", drink_id=id_dict["Drink"], compornent_id=compornent_id,
                        amount_number=amount_numbers[0][num])


        #################
        # DrinkTaste    #
        # DrinkTasteDoc #
        #################

        tastes = [ja_line["taste"], en_line["taste"], zh_line["taste"]]
        if not (tastes[0] in list(taste_db.keys())):
            drink_taste_id += 1
            taste_db[tastes[0]] = drink_taste_id
            push_in("DrinkTaste")
        for lang in range(3):
            push_in("DrinkTasteDoc", drink_taste_id=drink_taste_id, language=lang, taste=tastes[lang])


        ############
        # GrassDoc #
        # Grass    #
        ############

        glasses = [ja_line["glass"], en_line["glass"], zh_line["glass"]]
        cocktailTypes = [ja_line["cocktailType"], en_line["cocktailType"], zh_line["cocktailType"]]

        glass = glasses[0]
        if (glass == "ロックグラス" or
            glass == "タンブラー" or
            glass == "コリンズグラス" or
            glass == "ワイングラス" or
            glass == "ゴブレット" or
            glass == "ホットグラス" or
            glass == "ピルスナー"):
            total_amount = 120

        elif (glass == "カクテルグラス" or
              glass == "ソーサー型シャンパングラス" or
              glass == "フルート型シャンパングラス" or
              glass == "サワーグラス"):
            total_amount = 60

        elif (glass == "リキュールグラス" or
              glass == "ショットグラス"):
            total_amount = 30

        else:
            total_amount = 0

        if not (glasses[0] in list(glass_db.keys())):
            glass_id += 1
            glass_db[glasses[0]] = glass_id
            push_in("Grass", total_amount=total_amount)
        for lang in range(3):
            push_in("GrassDoc", grass_id=glass_db[glasses[0]], language=lang, name=glasses[lang],
                grass_type=cocktailTypes[lang])


        ###############
        # Category    #
        # CategoryDoc #
        ###############

        view_type = ja_line["cocktail_or_not"]
        categories = [ja_line["category"], en_line["category"], zh_line["category"]]

        if not (categories[0] in list(category_db.keys())):
            category_id += 1
            category_db[categories[0]] = category_id
            push_in("Category", view_type=view_type)
        for lang in range(3):
            push_in("CategoryDoc", category_id=category_db[categories[0]], language=lang,
                    name=categories[lang])


        ##########
        # Source #
        ##########

        reference_url = ja_line["reference_url"]
        source = ja_line["source"]
        push_in("Source", name=source, url=reference_url)


        ###########
        # Base    #
        # BaseDoc #
        ###########

        base = [ja_line["base"], en_line["base"], zh_line["base"]]
        if not (base[0] in list(base_db.keys())):
            base_id += 1
            base_db[base[0]] = base_id
            push_in("Base", image_url=image_url)
        for lang in range(3):
            push_in("BaseDoc", base_id=base_db[base[0]], language=lang, name=base[lang], description="")


        #####################
        # DrinkTechnique    #
        # DrinkTechniqueDoc #
        #####################

        method_categories = [ja_line["method_category"], en_line["method_category"], zh_line["method_category"]]
        if not (method_categories[0] in (method_category_db.keys())):
            drink_technique_id += 1
            method_category_db[method_categories[0]] = drink_technique_id
            push_in("DrinkTechnique")
        for lang in range(3):
            push_in("DrinkTechniqueDoc", drink_technique_id=method_category_db[method_categories[0]],
                    language=lang,
                    name=method_categories[lang], description="")


        #########
        # Drink #
        #########

        push_in("Drink", drink_taste_id=drink_taste_id, min_degree=min_degree, max_degree=max_degree,
                image_url=image_url, shop_url="", grass_id=glass_db[glasses[0]], category_id=category_db[categories[0]],
                source_id=id_dict["Source"], base_id=base_db[base[0]],
                drink_technique_id=method_category_db[method_categories[0]])


    print('-----CSVファイルとして出力-----')
    for key, value in result.items():
        with open('db_csv/{}.csv'.format(key), 'w', newline='', encoding='utf-8_sig') as f:
            csvwriter = csv.writer(f, delimiter=',')
            try:
                csvwriter.writerow(list(value[0].keys()))
                print("ok")
            except:
                print(key)
                print(list(value))
            for v in value:
                csvwriter.writerow(list(v.values()))