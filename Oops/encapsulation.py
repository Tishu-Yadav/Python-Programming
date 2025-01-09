"""Encapsulation
Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it."""
class Car:
    def __init__(self,brand,model):
        self.__brand=brand # __ double underscore is used to make it private.
        self.model=model
    def get_brand(self):# getter method for accesing private element.
        return self.__brand
my_car=Car("Toyota","Fortuner")
print(my_car.get_brand())