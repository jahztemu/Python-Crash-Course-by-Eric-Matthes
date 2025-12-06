from pathlib import Path
import json


def get_user_info():
    """Getting stored users"""
    path = "chapter_10\\module_text\\user.json"

    try:
        with open(path) as f:
            username = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        pass
    else:
        return username


def get_new_user():
    path = "chapter_10\\module_text\\user.json"
    name = input("what is your name? ")
    with open(path, "w") as f:
        json.dump(name, f)


def greet_user():
    """greet user"""
    username = get_user_info()
    if username:
        answer = input(f"Is your name {username} yes or no: ")
        response = answer.lower()
        if response == "yes":
            print(f"Welcome back {username} let kick off where we stopped")
        elif response == "no":
            username = get_new_user()
            print("We'll remember you when you come back!")
        else:
            print("Invalid input")
    else:
        username = get_new_user()
        print("We'll remember you when you come back!")


greet_user()
