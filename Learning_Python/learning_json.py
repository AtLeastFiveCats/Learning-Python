import json

foods = ["Pizza", "Cheese", "Dough"]
with open("files/food.json", "w") as f:
    json.dump(foods, f)