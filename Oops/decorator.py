"""Property Decorators
Problem: Use a property decorator in the Car class to make the model attribute read-only."""
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
    @property
    def model(self):
        return self.__model
    @property
    def model(self,value):
        self.model = value
my_car = Car("Toyota","Fortuner")#once setted
print(my_car.model)
my_car.model = "Innova"#raise error
