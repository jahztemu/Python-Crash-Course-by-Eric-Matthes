class restaurant:
    """description of restaurant"""

    def __init__(self, restaurant_name, *cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 143

    def describe_restaurant(self):
        """description of restaurant"""
        print(f'welcome to {self.restaurant_name.title()}')
        print('Cuisine type')
        for cuisine in self.cuisine_type:
            print(f' -{cuisine.title()}')

    def open_restaurant(self):
        """open restaurant"""
        print(f'{self.restaurant_name} is currently open')

    def set_number_served(self):
        """set number of served"""
        print(f'we have served over {self.number_served} customers')

    def increase_number_served(self, amount):
        """increase number of served"""
        self.number_served += amount
        print(f'we have currently served {self.number_served} customers')


my_rest = restaurant('midtown', 'rice', 'soup')
my_rest.describe_restaurant()
my_rest.open_restaurant()
my_rest.set_number_served()
my_rest.increase_number_served(2)

print('\n')  # 9.5

class user:
    """description of user"""

    def __init__(self, first_name, last_name, location,age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}')
        print(f'{self.location.title()}')
        print(f'{self.age} years old')
    def greet_user(self):
        print(f'Hey👋, {self.first_name.title()} {self.last_name.title()} welcome back')
        print(f'Your current location is {self.location} and age set to {self.age} years old')
    def increment_login_attempts(self, amount):
        self.login_attempts += amount
        print(f'You have logged in {self.login_attempts} times')
    def reset_login_attempts(self):
        self.login_attempts = 0

users = user('john', 'smith', 'london', 30)
users.increment_login_attempts(1)
users.increment_login_attempts(1)
users.increment_login_attempts(1)
users.increment_login_attempts(1)

users.reset_login_attempts()
users.increment_login_attempts(0)