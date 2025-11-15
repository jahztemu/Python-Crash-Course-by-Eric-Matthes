class restaurant:
    """description of restaurant"""

    def __init__(self, restaurant_name, *cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """description of restaurant"""
        print(f'welcome to {self.restaurant_name.title()}')
        print('Cuisine type')
        for cuisine in self.cuisine_type:
            print(f' -{cuisine.title()}')

    def open_restaurant(self):
        """open restaurant"""
        print(f'{self.restaurant_name} is currently open')


my_rest = restaurant('midtown', 'rice', 'soup')
my_rest.describe_restaurant()
my_rest.open_restaurant()

print('\n')  # 9.2

my_rest2 = restaurant('downtown', 'Cake', 'ice cream')
my_rest2.describe_restaurant()
my_rest2.open_restaurant()

print('\n')  # 9.3


class user:
    """description of user"""

    def __init__(self, first_name, last_name, location,age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}')
        print(f'{self.location.title()}')
        print(f'{self.age} years old')
    def greet_user(self):
        print(f'Hey👋, {self.first_name.title()} {self.last_name.title()} welcome back')
        print(f'Your current location is {self.location} and age set to {self.age} years old')

user1 = user('john', 'smith', 'london', 30)
user2 = user('odo', 'friday', 'lagos', 26)
user1.describe_user()
user1.greet_user()
print('\n')
user2.describe_user()
user2.greet_user()