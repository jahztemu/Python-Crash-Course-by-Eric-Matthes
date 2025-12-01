vacation = {}
poll = True

while poll:
    name = input('Thanks for participating in the poll, \nWhat is your name?')
    place = input('Now here is the question:\nIf you could visit one place in the world, where would you like to go?')
    vacation[name.title()] = place.title()

    done = input('Would you like to go again? Yes or No?')
    if done.lower() == 'no':
        poll = False

for name, place in vacation.items():
    print(f'My name is {name}, and I would like to visit {place}')
