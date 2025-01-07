'''Factorial Calculator
Problem: Compute the factorial of a number using a while loop.'''
num = int(input("Enter a Number :"))
n = num
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial of",n,"is",fact)