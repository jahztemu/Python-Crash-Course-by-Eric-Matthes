cars = ["toyota", "benz", "tesla"]
unavailable_cars = ["benz"]

if cars:
    for car in cars:
        if car in unavailable_cars:
            print(f"{car} is currently unavailable")
        else:
            print(f"{car} is available")
else:
    print("Input a car")


mod = []

for mpc in range(10):
    mpcs = {"color": "yellow", "point": "green"}
    mod.append(mpcs)

for mob in mod[:5]:
    print(mob)


favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_languages.items():
    if len(languages) == 2:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        for lang in languages:
            print(f"{name.title()}'s language is {lang}")
