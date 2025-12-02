sandwich_orders = ['bacon', 'barbecue', 'beirute', 'bifana']
finished_sandwiches = []

while sandwich_orders:
    verify_order = sandwich_orders.pop()
    print(f'{verify_order} is ready for collection')
    finished_sandwiches.append(verify_order)
print(f'This sandwiches are ready for collection')
for order in finished_sandwiches:
    print(f'{order}')

print('\n')  # 7.9

sandwich_orders = ['pastrami','bacon', 'barbecue','pastrami', 'beirute', 'bifana', 'pastrami']

print('The deli has  has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
