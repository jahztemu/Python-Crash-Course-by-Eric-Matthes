# 6.1
rivers = {}

rivers["River Nile"] = "Egypt"
rivers["River Niger"] = "Nigeria"
rivers["Amazon River"] = "Brazil"

for river, place in rivers.items():
    print(f"The {river} runs through {place}")

for river in rivers.keys():
    print(river)

for place in rivers.values():
    print(place)

print("\n")  # 6.6

queue = ["jane", "fave", "dave", "jake", "rick", "gift", "lois"]

tested = {"jane": "python", "dave": "c", "rick": "java"}

for name in queue:
    if name in tested.keys():
        language = tested[name]
        print(
            f"{name.title()} it seems you have taken the test and chooses {language.title()} as "
            "your favorite language"
        )
    else:
        print(f"{name.title()} you are welcome please choose your favorite language")
