alien_color = "green"

if alien_color == "green":
    print("Player just earned 5 points")

if alien_color == "red":
    print("this version fails")


# 5.4
alien_color == "red"

if alien_color == "green":
    print("player just earned 5 points")
if alien_color != "green":
    print("player just earned 10 points")

if alien_color == "green":
    print("player just earned 5 points")
else:
    print("player just earned 10 points")

# 5.5
print("\n")
alien_color = "red"

if alien_color == "green":
    print("player just earned 5 points")
elif alien_color == "yellow":
    print("player just earned 10 points")
elif alien_color == "red":
    print("player just earned 15 points")

print("\n")

alien_color = "yellow"
if alien_color == "green":
    print("player just earned 5 points")
elif alien_color == "yellow":
    print("player just earned 10 points")
elif alien_color == "red":
    print("player just earned 15 points")

print("\n")

alien_color = "green"

if alien_color == "green":
    print("player just earned 5 points")
elif alien_color == "yellow":
    print("player just earned 10 points")
elif alien_color == "red":
    print("player just earned 15 points")

# 5.6
age = 4
if age < 2:
    print("you are a baby")
elif age < 4:
    print("you are a toddler")
elif age < 13:
    print("you are a kid")
elif age < 20:
    print("you are a teenager")
elif age < 65:
    print("you are an adult")
else:
    print("you are an elder")


# 5.7

fav_fruit = ["apple", "banana", "grape", "strawberry", "blueberry"]
fruit = ["grape"]
for xx in fruit:
    if xx in fav_fruit:
        print(f"{xx.title()} fruit is in favorite fruit list")
    else:
        print(f"{xx.title()} fruit is not in favorite fruit list")
