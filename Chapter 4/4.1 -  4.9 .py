#4.1
foods = [
    'Rice', 'salad', 'Fries',
    'fish']
for food in foods:
    print(f'{food} is among some of the few dishes in the cafeteria')
    print('some of the workers really love the dishes we offer')

print('/////')

#4.2
pets = [
    'dog','cat','hamaster',
    'Parrot','Rabbit']
for pet in pets:
    print(f'{pet.title()} is an example of friendly pet')
print('Any of this animals would make a great pet')

print('/////')

#4.3
for value in range(1,21):
    print(value)

print('/////')

#4.4
#for xc in range(1,1000001):
    #print(xc)

#4.5
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('/////')

#4.6
#method 1
odd_num = list(range(1,20,2))
print(odd_num)

#method 2
nums =[]
for value in range (-1,9):
    numa = value + 1.5
    num = numa * 2
    nums.append(int(num))
print(nums)

#method 3
numbers = [value +2  for value in range(-1,19,2)]
print(numbers)

print('/////')

#4.7
#method 1
numbers = [value *3 for value in range(1,30)]
print(numbers)

#method 2
mult = []
for value in range(1,30):
    num = value *3
    mult.append(num)
print(mult)

print('/////')

#4.8
xx = []
for value in range (1,10):
    num = value **3
    xx.append(num)
print(xx)

print('/////')

#4.9
number = [value **3 for value in range (1,10)]
print(number)
