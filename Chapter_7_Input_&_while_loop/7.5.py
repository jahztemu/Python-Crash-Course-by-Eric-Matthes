text = 'Please enter your age to determine the price of your ticket'
while True:
    ages = input(text)
    age = int(ages)
    if age <= 3:
        print('Your ticket price is free')
    elif age <= 12:
        print('Your ticket price is $10')
    elif age > 12:
        print('Your ticket price is $15')

