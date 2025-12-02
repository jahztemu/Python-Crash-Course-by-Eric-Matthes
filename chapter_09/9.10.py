import modules.car as car

my_tesla = car.ElectricCar("tesla", "model s", 2025)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.update_odometer(200)
my_tesla.read_odometer()
my_tesla.increment_odometer(100)
my_tesla.read_odometer()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
