prompt = 'Enter a number let tell you the multiples'
values = input(prompt)
value = int(values)
x = 1

while True:
    print(f'{value} x {x} = {x*value}')
    x += 1