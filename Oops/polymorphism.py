"""Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors."""
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def fuel_type(self):#Polymorphism
        return "Petrol or Diesel"

class ElectricCar(Car):#Inheritence
    def __init__(self,brand,model,battery_size):
        self.battery_size=battery_size
        super().__init__(brand,model)#for Inheritance
    def fuel_type(self):#Polymorphism
        return "Electric Charge"
my_car = Car("","")
my_car2 = ElectricCar("","","")
print(my_car.fuel_type())
print(my_car2.fuel_type())