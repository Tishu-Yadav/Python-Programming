'''Prime Number Checker
Problem: Check if a number is prime.'''
num = int(input("Enter a Number :"))
is_prime = True
for i in range (2,num):
    if (num % i) == 0:
        is_prime = False
        break
if is_prime == True:
    print(num ,"is a Prime Number")
else:
    print(num ,"is not a Prime Number")    