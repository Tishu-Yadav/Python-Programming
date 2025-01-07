"""Function Returning Multiple Values
Problem: Create a function that returns both the area and circumference of a circle given its radius."""
import math
def area(r):
    area= round(math.pi*(r**2),2)
    circumference = round(2*math.pi*r,2)
    return area,circumference
r = int(input("Enter Radius of Circle:"))
result,circum = area(r)
print("Area of Circle is :",result,"Circumference is :",circum)