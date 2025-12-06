import json

user = input("What is your favorite number: ")
path = "chapter_10\\module_text\\fav.json"

with open(path, "w") as f:
    json.dump(user, f)

with open(path) as f:
    info = json.load(f)

print(f"I know your favorite number! It's {info}")
