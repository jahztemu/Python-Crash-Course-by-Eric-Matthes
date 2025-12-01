prompt = 'Now please select pizza toppings'
prompt += '\nwhich toppings will you like to add?'
prompt += '\n Enter toppings or Quit'
x=1
while x <=5:
    message = input(prompt)
    if message.lower() == 'quit':
       break
    else:
        print(message)
    x+=1