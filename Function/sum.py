'''Function with Multiple Parameters
Problem: Create a function that takes two numbers as parameters and returns their sum.'''
def sum(a,b):
    return a+b
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
result = sum(a,b)
print("Sum of",a,"and",b,"is :",result)