from pathlib import Path
import json

path = "chapter_10\\module_text\\fav.json"

try:
    with open(path) as f:
        info = json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    user = input("What is your favorite number: ")
    with open(path, "w") as f:
        json.dump(user, f)
else:
    print(f"I know your favorite number! It's {info}")
