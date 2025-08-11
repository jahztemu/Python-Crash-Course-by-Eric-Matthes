# 6.7
from warnings import catch_warnings


dave = {"firstname": "Dave", "lastname": "jacob", "age": 20, "city": "new york"}
jake = {"firstname": "jake", "lastname": "nelson", "age": 18, "city": "paris"}
jack = {"firstname": "jackson", "lastname": "edward", "age": 19, "city": "london"}

people = [dave, jake, jack]


for name in people:
    for names, details in name.items():
        print(f"{names}:{details}")

# 6.8
pet_1 = {}
pet_2 = {}
pet_3 = {}
