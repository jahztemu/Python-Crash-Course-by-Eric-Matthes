cars = ["toyota", "benz", "tesla"]
unavailable_cars = ["benz"]

if cars:
    for car in cars:
        if car in unavailable_cars:
            print(f"{car} is currently unavailable")
        else:
            print(f"{car} is available")
else:
    print("Input a car")

numbers = []
