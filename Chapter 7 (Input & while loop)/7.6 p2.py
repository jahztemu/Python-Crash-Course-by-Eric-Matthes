text = 'Please enter your age to determine the price of your ticket'
text += '\nEnter your age to determine the price of your ticket'
x = 1
while x <= 5:
    age = input(f"Attempt left {5 - x}:\n{text}")
    if age.lower() == 'quit':
        print('You just ended the program')
        break
    ages = int(age)
    if ages <= 3:
        print('Your ticket price is free')
    elif ages <= 12:
        print('Your ticket price is $10')
    elif ages > 12:
        print('Your ticket price is $15')
    x += 1
