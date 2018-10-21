# -*- coding: utf-8 -*-
import json
from function import make_db_csv

# 全ての言語のjsonデータを格納
# あとでmake_db_csvになげる
all_lang_list = []

for path_num in range(3):
    if (path_num == 0):
        f = open('format_data/suntoryCocktailRecipe_formatData_ja.json', 'r')
    else:
        f = open(['translation_data/suntoryCocktailRecipe_translationData_en.json',
                  'translation_data/suntoryCocktailRecipe_translationData_zh.json'][path_num - 1], 'r',
                 encoding="utf-8_sig",
                 errors="ignore")
    json_data = json.load(f)
    all_lang_list += [json_data]


# db用csv作成
make_db_csv(all_lang_list)
