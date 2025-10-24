#7.4
prompt = 'Now please select pizza toppings'
prompt += '\nwhich toppings will you like to add?'
prompt += '\n Enter toppings or Quit'

while True:
    message = input(prompt)
    if message.lower() == 'quit':
       break
    else:
        print(message)
