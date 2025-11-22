# 8.1
def greeting():
    """greeting function"""
    print(
        "In this chapter we learn the fundamental and complexity of functions in python "
    )


greeting()

print("\n")  # 8.2


def favorite_book(title):
    """my favorite book"""
    print("My favorite book is " + title)


favorite_book("Python Programming")

print("\n")  # 8.3


def make_shirt(size, text):
    """my shirt"""
    print(f'The shirt size is {size} and the printed text should be "{text}"')


make_shirt("Large", "Happy Birthday")

print("\n")  # 8.4


def large_shirt(size="large", text="I love Python"):
    """my large shirt"""
    print(f'The shirt size is {size} and the printed text should be "{text}"')


large_shirt()
large_shirt(size="medium")
large_shirt(text="I love C")

print("\n")  # 8.5


def describe_city(city="", country="UK"):
    """my city and country"""
    print(f"{city} is in {country}")


describe_city("Manchester")
describe_city(city="London")
describe_city(city="New York", country="USA")
describe_city("Lagos", "Nigeria")
