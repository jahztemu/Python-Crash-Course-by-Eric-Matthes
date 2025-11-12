def sandwich(size, *tops):
    """Making a Sandwich"""
    print(f'pizza size: {size} inches')
    print('And has the  following toppings:')
    for topping in tops:
        print(f' -{topping}')

sandwich(16,'cheese','Green peppers','Mushrooms','pepperoni')

def build_profile(first, last, **user_info):
    """Build a profile with some basic info"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile('John', 'Smith', level = 500, department = 'Mechanical Engineering')
print(profile)

def make_car(manufacturer, model, **info):
    """Make a car"""
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info

car = make_car('Toyota', 'SUV', color = 'White', tow_package = True)
print(car)