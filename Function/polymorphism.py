'''Polymorphism in Functions
Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.'''
def multiply(a,b):
    return a*b
print(multiply(2,5))
print(multiply("Love ",5))
print(multiply(2,"I Love You "))