#3.10
places = ['London','Tokoy','Lagos','Manila','Rabat','New york','Abuja']
places.pop()
places.append('Cape town')
places.insert(7,'Java')
places.remove('Java')
print(places)

print(f'{sorted(places)} This list has been sorted aphbatically')
print(f'{sorted(places,reverse=True)} This list is sorted and reverse')
print(f'{places} You can see the changes does not affect the original list')

places.reverse()
print(f'{places} The list has been permanently reverse')

places.reverse()
print(f'{places} The list has been revereted to it original form')

places.sort()
print(f'{places} The list has been permanently sorted aphbaticaly')

places.sort(reverse=True)
print(f'{places} This is a permanently sorted and reversed list')

print(f'This list contain {len(places)} places, places like; \n{places[1]}, \n{places[4]}, \n{places[6]} and so on')

#3.11
#-print('f This list contain {len(places)} places')
#line 28 is an example off an error code
