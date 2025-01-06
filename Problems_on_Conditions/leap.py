'''Leap Year Checker
Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).'''
Year = int(input('Enter a Valid Year:'))
if (Year % 400 == 0) or (Year % 4 == 0 and Year % 100 !=0):
    print("Entered Year",Year,"Is Leap Year")
else:
    print(Year,"is not a Leap Year")