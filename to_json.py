import json

def dict_wrapper(ing):
    eff_key = ["primary", "secondary", "tertiary", "quarternary"]
    eff_val = ing[1:5]
    eff_dic = dict(zip(eff_key, eff_val))


    tot_key = ["name", "effects", "weight", "value", "obtained", "minimal"]

    if ing[0][-1] == '\u002A':
        minimal = 'dawngard'
        ing[0] = ing[0].replace('\u002A', '')

    elif ing[0][-1] == '\u2020':
        minimal = 'hearthfire'
        ing[0] = ing[0].replace('\u2020', '')

    elif ing[0][-1] == '\u2021':
        minimal = 'dragonborn'
        ing[0] = ing[0].replace('\u2021', '')
    else:
        minimal = None

    tot_val = [ing[0]] + [eff_dic] + ing[5:] + [minimal]
    tot_dic = dict(zip(tot_key, tot_val))

    return tot_dic

ingredient_raw_file = open("./ingredients.html", "r", encoding="UTF-8")
lines = ingredient_raw_file.readlines()

total = []
ingredient = []

# read html file and make string list
for line in lines:
    if line != '\n':
        ingredient.append(line.replace('\n', ''))
    else:
        total.append(ingredient)
        ingredient = []

# string list -> dictionary list
for _ in range(0, len(total)):
    total.append(dict_wrapper(total.pop(0)))

with open("result.json", "w") as json_file:
    json.dump(total, json_file, indent=4)