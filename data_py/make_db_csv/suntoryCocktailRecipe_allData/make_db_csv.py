# -*- coding: utf-8 -*-
import requests
import csv
import json
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse

def push_in(table, **keyword_arguments):
    table += [keyword_arguments]

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
    JA = 0
    EN = 1
    ZH = 2
    ja_lines = all_lang_list[JA]
    en_lines = all_lang_list[EN]
    zh_lines = all_lang_list[ZH]
    drink_id = 0
    drink_taste_id = 0
    grass_id = 0
    category_id = 0
    source_id = 0

    for i in range(l):
        ja_line = ja_lines[i]
        en_line = en_lines[i]
        zh_line = zh_lines[i]

        Drink_id = i+1
        
        
        #Drink
        alcohol_percentage = ja_line["alcohol_percentage"]
        if ("強" in alcohol_percentage):
            max_degree = 40
            min_degree = 25
        elif ("普通" in alcohol_percentage):
            max_degree = 25
            min_degree = 8
        elif ("弱"　in alcohol_percentage):
            max_degree = 8
            min_degree = 1

        imga_url = ja_line["image"]


        #DrinkCompornent
        #DrinkCompornent
        #Compornent
        #CompornentDoc
        for j in range(1, 11):
            if (exec("(ja_line['ingredient{}'])".format(j))):
                ja_ingredients += [j-1]
                
        #DrinkName
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="drink_name"]))
        ja_drink_name = ja_line["drink_name"]
        en_drink_name = en_line["drink_name"]
        zh_drink_name = zh_line["drink_name"]
        priority = ja_line["priority"]

        #DrinkDoc
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="description"]))
        ja_description = ja_line["description"]
        en_description = en_line["description"]
        zh_description = zh_line["deescription"]
        ##ja_description = ...
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="method_detail"]))
        ja_method_detail = ja_line["method_detail"]
        en_method_detail = en_line["method_detail"]
        zh_method_detail = zh_line["method_detail"]
        ##ja_method_detail = ...
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="color"]))
        ja_color = ja_line["color"]
        en_color = en_line["color"]
        zh_color = zh_line["color"]

        #DrinkTechnique

        #DrinkTechniqueDoc
        ja_method_category = ja_line["method_category"]
        en_method_category = en_line["method_category"]
        zh_method_category = zh_line["method_category"]

        #DrinkTaste

        #DrinkTasteDoc
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="taste"]))
        ja_taste = ja_line["taste"]
        en_taste = en_line["taste"]
        zh_taste = zh_line["taste"]

        #Grass
        total_amount = -9999

        #GrassDoc
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="glass"]))
        ja_glass = ja_line["glass"]
        en_glass = en_line["glass"]
        zh_glass = zh_line["glass"]
        ##ja_glass = ...
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="cocktailType"]))
        ja_cocktailType = ja_line["cocktailType"]
        en_cocktailType = en_line["cocktailType"]
        zh_cocktailType = zh_line["cocktailType"]
        ##ja_cocktailType = ...

        #Category
        view_type = ja_line["cocktail_or_not"]


        #CategoryDoc
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="category"]))
        ja_category = ja_line["category"]
        en_category = en_line["category"]
        zh_category = zh_line["category"]
        ##ja_category = ...
    
        #Source
        reference_url = ja_line["reference_url"]
        source = ja_line["source"]

        #Base


        #BaseDoc
        #for p in range(3): exec("{lang}_{name} = {lang}_line['{name}']".format([lang=["ja","en","zh"][p], name="base"]))
        ja_base = ja_line["base"]
        en_base = en_line["base"]
        zh_base = zh_line["base"]
        ##ja_base = ...






