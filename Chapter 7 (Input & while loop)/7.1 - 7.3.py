#7.1
incar=input('what kind of rental car do you want?')
print(f"Let me see if {incar} is available")

print('\n')#7.2
people=input('how many people are sitting at a table')
people=int(people)

if people >= 8:
    print(f'You have to wait for a table cause no current table for {people} people')
else:
    print(F'Your table for {people} is ready, when will you be visiting')

print('\n')#7.3
numbers=input('please enter a number')
numbers=int(numbers)
if numbers % 10 == 0:
    print(f'{numbers} is a multiple of 10')
else:
    print(f'{numbers} is not a multiple of 10')
