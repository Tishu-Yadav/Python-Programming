'''Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.'''
number = int(input("Enter a Number: "))
sum = 0
for i in range(1,number+1):
    if (i % 2) == 0:
        sum = sum + i
print("Total Sum of Even Numbers upto",number,"is ",sum)