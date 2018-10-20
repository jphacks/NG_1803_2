# import json
# import pprint

# f = open('original_data/suntoryCocktailRecipe_allData_20181010.json', 'r')
# json_dict = json.load(f)
# pprint.pprint(json_dict, width=40)

# # print(json.dumps(json_dict, indent=2))

a = 0
exec("global {}".format(A))

def f():
    A = -1
    exec("""global {}""".format(A))

f()

print(A)