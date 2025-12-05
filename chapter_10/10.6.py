print("A SIMPLE CALCULATOR")
first_number = input("Enter the first number: ")
operator = input("Enter the operator (+, -, *, /): ")
second_number = input("Enter the second number: ")

try:
    if operator == "+":
        print(int(first_number) + int(second_number))
    elif operator == "-":
        print(int(first_number) - int(second_number))
    elif operator == "*":
        print(int(first_number) * int(second_number))
    elif operator == "/":
        print(int(first_number) / int(second_number))
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
