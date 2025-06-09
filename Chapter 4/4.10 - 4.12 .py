#4.10
city = [
    'london','lagos','abuja',
    'tokyo','rabat','ozoro',
    'kwale','kaduna','jos']
for cities in city[:3]:
    print(cities.title())

print('-----')

for cities in city[3:6]:
     print(cities.title())

print('-----')

for cities in city[6:]:
    print(cities.title())

print('/////')

#4.11
foods = [ 
    'Rice', 'salad',
    'Fries', 'fish']
friend_food = foods[:]

foods.append('pizza')
friend_food.append('snacks')

print('example of foods are:')
for xx in foods:
    print(xx.title())



print('-----')

print('Exampl of food friends eat')
for xx in friend_food:
    print(xx.title())

#4.12
