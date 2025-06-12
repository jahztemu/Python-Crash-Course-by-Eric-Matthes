# 5.1
car = "bmw"
print("Is car == 'BMW' I predict True")
print(car == "BMW")
print("Is car == 'Audi', I predict False")
print(car == "Audi")

food = "pizza"
print("\nis food != 'pizza', I predict False")
print(food != "pizza")
print("Is car != 'rice', I predict True")
print(food != "rice")

num = 7
print("\nis number < 7, I predict False")
print(num < 7)
print("Is number <= 7, I predict True")
print(num <= 7)
print("Is number > 7, I predict False")
print(num > 7)
print("Is number >= 7, I predict True")
print(num >= 7)

num = 10
print("\nIs number == 10, I predict True")
print(num == 10)
print("Is number > 12, I predict False")
print(num > 12)
print("Is number < 12, I predict True")
print(num < 12)

# 5.2
city = "lagos"
print(f"\ncity == lagos {city == "lagos"}")
print(f"city != lagos {city != "lagos"}")

car = "Tesla"
print(f"\ncar == tesla {car == "tesla"}")
print(f"car == Tesla {car == "Tesla"}")
car = car.lower()
print(f"\ncar == tesla {car == "tesla"}")
print(f"car == Tesla {car == "Tesla"}")

num = 10
print("\nThe number is 10")
print(f"Number < 12 {num < 12}")
print(f"Number > 12 {num > 12}")
print(f"Number <= 10 {num <= 10}")
print(f"Number >= 10 {num >= 10}")
print(f"Number == 10 {num == 10}")
print(f"Number != 10 {num != 10}")
print(f"Number == 11 {num == 11}")
print(f"Number != 11 {num != 11}")


first_name = "logan"
last_name = "jane"
print("\n")
print(first_name == "logan" and last_name == "jane")
print(first_name == "logan" or last_name == "jane")

print("\n")
countries = ["omen", "japan", "usa", "england"]
print("omen" in countries)

country = "nigeria"
if country not in countries:
    print("Nigeria not in list")
