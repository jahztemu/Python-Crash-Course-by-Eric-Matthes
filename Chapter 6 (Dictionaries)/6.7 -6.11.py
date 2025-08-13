# 6.7
dave = {"firstname": "Dave", "lastname": "jacob", "age": 20, "city": "new york"}
jake = {"firstname": "jake", "lastname": "nelson", "age": 18, "city": "paris"}
jack = {"firstname": "jackson", "lastname": "edward", "age": 19, "city": "london"}

people = [dave, jake, jack]


for name in people:
    for names, details in name.items():
        print(f"{names}:{details}")

print("\n")  # 6.8
pet_1 = {"animal": "cat", "owner": "fave"}
pet_2 = {"animal": "dog", "owner": "dave"}
pet_3 = {"animal": "parrot", "owner": "jake"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for animals, owner in pet.items():
        print(f"{animals}:{owner}")

print("\n")  # 6.9
favorite_places = {
    "dave": {"fav_place": ["london", "paris", "tokyo"]},
    "jack": {"fav_place": ["kentucky", "new york", "new jersey"]},
    "harry": {"fav_place": ["lagos", "abuja", "asaba"]},
}

for key, value in favorite_places.items():
    for place in value.values():
        print(f"\n{key.title()} favorite places are:")
        for city in place:
            print(f"{city.title()}")

print("\n")  # 6.10
numbers = {}

numbers["james"] = [4, 56, 7]
numbers["jake"] = [5, 76, 5]
numbers["sarah"] = [5, 77]
numbers["vale"] = [64, 77, 1]
numbers["divine"] = [33, 40]

for name, number in numbers.items():
    print(f"{name.title()} favorite numbers are:")
    for value in number:
        print(value)

print("\n")  # 6.11
cities = {
    "london": {
        "country": "england",
        "population": "8.9 million",
        "fact": "oldest subway in the world",
    },
    "paris": {
        "country": "italy",
        "population": "2 million",
        "fact": "know as city of Love",
    },
    "lagos": {
        "country": "nigeria",
        "population": "17.2 million",
        "fact": "sixth largest city in the world",
    },
}

for city, fact in cities.items():
    print(f"\nCity to explore is {city.title()}:")
    for place, details in fact.items():
        print(f"{place.title()}:{details.title()}")
