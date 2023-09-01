import json

with open("food.json") as f:
    food_list = json.load(f)
print(food_list)