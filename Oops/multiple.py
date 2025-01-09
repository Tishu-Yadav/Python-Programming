"""Multiple Inheritance
Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance."""
class Battery:
    def battery_info(self):
        return "This is Battery"
class Engine:
    def engine_info(self):
        return "This is Engine"
class ElectricCar(Battery,Engine):
    pass
my_car = ElectricCar()
print(my_car.battery_info(), my_car.engine_info())
print(isinstance(my_car,Battery))
print(isinstance(my_car,Engine))
print(isinstance(my_car,ElectricCar))