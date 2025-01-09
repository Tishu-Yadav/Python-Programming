"""Class Variables
Problem: Add a class variable to Car that keeps track of the number of cars created."""
class Car:
    total_car =0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car += 1
my_car = Car("","")
my_car2=Car("","")
my_car3 =Car("","")
print(my_car.total_car)