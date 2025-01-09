"""Static Method
Problem: Add a static method to the Car class that returns a general description of a car."""
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
    @staticmethod
    def general_description():
        return "Cars are means of Transport"
my_car = Car("Maruti","Alto")
print(my_car.brand, my_car.model, my_car.full_name(), my_car.general_description())