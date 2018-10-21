import json
import csv

# fw = open('translation_data/suntoryCocktailRecipe_translationData_zh.json', 'w', encoding='UTF-8')
# ココ重要！！
f = open('translation_data/suntoryCocktailRecipe_translationData_zh.json', 'r',
         encoding='utf_8_sig')
json_data = json.load(f)

with open('db_csv/test' + '.csv', 'w', newline='', encoding='utf_8_sig') as f:
    # dialectの登録
    csv.register_dialect('dialect01')
    # DictWriter作成
    writer = csv.DictWriter(f, fieldnames=json_data[0].keys(), dialect='dialect01')
    # CSVへの書き込み
    writer.writeheader()
    for json_data in json_data:
        writer.writerow(json_data)