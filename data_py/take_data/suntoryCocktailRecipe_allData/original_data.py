# coding:utf-8
import urllib
import urllib3
from bs4 import BeautifulSoup
import certifi
import json

#################################################################
# サントリーのカクテル一覧から情報をスクレイピングするプログラム
#################################################################

# アクセスするURL
url = "https://cocktailrecipe.suntory.co.jp/wnb/cocktail/unique"

urlHost = 'https://cocktailrecipe.suntory.co.jp'

# httpsの証明書検証を実行している
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

baseList = [
    "ジン",
    "ウォッカ",
    "テキーラ",
    "ラム",
    "リキュール",
    "ワイン",
    "ビール",
    "ウイスキー",
    "その他"
]

allCocktailData = []

for baseNum in range(1, 9):     # 上のbaseListで何番目か（1スタート）
    base = baseList[baseNum - 1]
    index = 1
    flag = True
    print("########################################")
    print("baseNum: " + str(baseNum))
    print("base: " + base)
    print("index: " + str(index))
    print("flag: " + str(flag))
    print("########################################")
    while(flag):
        print(index)
        #################################################################
        # ①サントリーのカクテル一覧ページからカクテルごとのURLを取得
        #################################################################

        query = {
            'head': 'HEAD',
            'start': index,     # そのページにレシピがないとなったらやめる
            'count': 1,     # そのページに表示する数だから好きに設定できる
            'base': "0" + str(baseNum)    # 01~09まで
            }
        cocktailId = query["start"]*10 + baseNum


        r = http.request('GET', url + '?' + urllib.parse.urlencode(query))

        soup = BeautifulSoup(r.data, 'html.parser')

        cocktailUrl = soup.find_all("table", attrs={"summary": "layout"})[0]

        flag = cocktailUrl.find_all("tr", attrs={"class": "odd"})
        # print("\nflag: " + str(flag) + "\n")
        if not flag:
            break

        cocktailUrl = cocktailUrl.find_all("a")[0]['href']
        #####################################################
        # ②それぞれのカクテルページから必要情報を取得
        #####################################################
        referenceUrl = urlHost + cocktailUrl

        r = http.request('GET', referenceUrl)

        soup = BeautifulSoup(r.data, 'html.parser')

        # 必要箇所の全データを取得
        data = soup.find_all("div", attrs={"class": "detail_recipe"})[0]
        # カクテル名（日本語）
        name_JP = data.find_all("h2")[0].string
        # 画像
        img = data.find_all("img")[0]["src"]
        # 諸情報
        dr_cktl_list = data.find_all("div", attrs={"class": "dr_cktl_list"})[0].find_all("dd")
        dr_cktl_list = [i.string.replace('\n', '').replace('\r', '') for i in dr_cktl_list]

        cocktailType = dr_cktl_list[0]
        glass = dr_cktl_list[1]
        taste = dr_cktl_list[2]
        color = dr_cktl_list[3]
        alcoholPercentage = dr_cktl_list[4]
        preparation = dr_cktl_list[5]

        # 材料の配列
        ingredient = data.find_all("div", attrs={"class": "dr_ingredient"})[0].find_all("dt")
        ingredient = [i.string for i in ingredient]
        # 量の配列
        measure = data.find_all("div", attrs={"class": "dr_ingredient"})[0].find_all("dd")
        measure = [i.string for i in measure]
        #作り方
        howTo = data.find_all("div", attrs={"class": "dr_howto"})[0].find_all("li")
        howTo = [i.string for i in howTo]
        # ワンポイント
        onePoint = data.find_all("div", attrs={"class": "dr_onepoint"})[0].find_all("p")[0].string

        cocktailData = {
            "base": base,
            "cocktailId": cocktailId,
            "name_JP": name_JP,
            "cocktailType": cocktailType,
            "glass": glass,
            "taste": taste,
            "color": color,
            "alcoholPercentage": alcoholPercentage,
            "preparation": preparation,
            "howTo": howTo,
            "img": img,
            "ingredient": ingredient,
            "measure": measure,
            "onePoint": onePoint,
            "referenceUrl": referenceUrl
        }
        print(cocktailData)
        allCocktailData.append(cocktailData)

        index += 1

print('-----JSONファイルとして出力-----')
fw = open('original_data/suntoryCocktailRecipe_allData.json', 'w')
# ココ重要！！
# json.dump関数でファイルに書き込む
json.dump(allCocktailData, fw, ensure_ascii=False)
