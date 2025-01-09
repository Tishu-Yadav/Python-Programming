"""Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size."""
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        self.battery_size=battery_size
        super().__init__(brand,model)

my_car = Car("Toyota","Fortuner")
my_Tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_car.model ,my_car.brand)
print(my_Tesla.brand ,my_Tesla.model ,my_Tesla.battery_size)