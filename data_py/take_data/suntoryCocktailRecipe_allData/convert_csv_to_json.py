# coding:UTF-8
import json
import csv

json_list = []
json_data = {}

# CSVファイルのロード
with open('adjust_format_data/お酒データ追加あり201810241333.csv', 'r', encoding='utf_8_sig') as f:
    # list of dictの作成
    for line in csv.DictReader(f):
        json_list.append(line)

    json_data = json_list

fw = open('adjust_format_data/お酒データ追加あり201810241333.json', 'w', encoding='utf_8_sig')
# JSONへの書き込み
json.dump(json_data, fw, ensure_ascii=False)
