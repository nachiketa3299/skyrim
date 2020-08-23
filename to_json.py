def wrapper(ing):
    eff = [ing[1:5]]
    wrp = [ing[0]] + eff + ing[5:] 
    return wrp

ingredient_raw_file = open("./ingredients.html", "r", encoding="UTF-8")
lines = ingredient_raw_file.readlines()

total = []
ingredient = []
for line in lines:
    if line != '\n':
        ingredient.append(line.replace('\n', ''))
    else:
        total.append(ingredient)
        ingredient = []


for _ in range(0, len(total)):
    total.append(wrapper(total.pop(0)))

print(total)