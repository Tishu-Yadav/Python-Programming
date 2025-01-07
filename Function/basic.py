"""Basic Function Syntax
Problem: Write a function to calculate and return the square of a number."""
def square(n):
    return n**2
n = int(input("Enter a Number:"))
result = square(n)
print("Square of",n,"is :",result)