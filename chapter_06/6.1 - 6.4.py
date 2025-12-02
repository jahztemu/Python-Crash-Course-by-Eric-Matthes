# 6.1
dave = {"firstname": "Dave", "lastname": "jacob", "age": 20, "city": "new york"}

firstname = dave.get("firstname")
lastname = dave.get("lastname")
age = dave.get("age")
city = dave.get("city")

print(f"This user firstname is {firstname}. ")
print(f"This user lastname is {lastname}. ")
print(f"This user age is {age}. ")
print(f"This user city is {city}. ")

print("\n")  # 6.2
numbers = {}

numbers["james"] = 4
numbers["jake"] = 3
numbers["sarah"] = 14
numbers["vale"] = 22
numbers["divine"] = 89

print(f'james favorite number is {numbers["james"]}')
print(f"jake favorite number is {numbers['jake']}")
print(f"sarah favorite number is {numbers['sarah']}")
print(f'vale favorite number is {numbers["vale"]}')
print(f'divine favorite number is {numbers["divine"]}')

print("\n")  # 6.3
glossary = {
    "comparison": "Comparison are use to evaluate numbers and words",
    "print": "It is use to call out a program to be seen in the terminal",
    "list": "As this name stands it is the creation list this can be numbers, words or"
    " anything",
    "operators": "This are symbols that can perform operations this operator consist of "
    "comparison operators, logical operators e.t.c",
    "variable": "This can be consider as name of operation is the core giving name to an assign "
    "functions",
}

print(f'Comparison: \n{glossary["comparison"]}')
print(f"print: \n{glossary['print']}")
print(f'List:\n{glossary["list"]}')
print(f'Operators:\n{glossary["operators"]}')
print(f'Comparison:\n{glossary["comparison"]}')
print(f'Variable:\n{glossary["variable"]}')

print("\n")  # 6.4

glossary["loop"] = (
    "Loop are function that help run through all the giving task without calling and"
    "an running one by one"
)
glossary["terminals"] = "This is place in your code environment where code are display"
glossary["extension"] = (
    "This are tools and components that help developers enhanced and make better code"
)


for key, value in glossary.items():
    print(f"\n{key}: \n{value}.")
