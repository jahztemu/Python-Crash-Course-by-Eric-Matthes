# 5.8
username = ["jake", "ben", "clinton", "marvel", "admin"]

for user in username:
    if user == "admin":
        print("welcome Admin")
    else:
        print(f"{user.title()} welcome, how may we be of service")

print("\n")  # 5.9
username = []

if username:
    for user in username:
        if user == "admin":
            print("welcome Admin")
        else:
            print(f"{user.title()} welcome, how may we be of service")
else:
    print("We need to find more users")

print("\n")  # 5.10

current_users = ["jake", "ben", "clinton", "marvel", "happy", "rick", "dave"]
new_users = ["kate", "berry", "jake", "gale", "BEN"]

for names in new_users:
    if names.lower() in current_users:
        print(f"{names.title()}, already exist as a user")
    else:
        print(
            f"{names.title()} you are welcome you will soon receive your new user bonus"
        )

print("\n")  # 5.11
# number = list(range 1, 10)

numbers = []

for number in range(1, 10):
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# 5.13
# using Black and flake8
