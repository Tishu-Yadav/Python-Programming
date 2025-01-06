'''Grade Calculator
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).'''
Score = int(input("Enter Your Marks:"))
if Score >100:
    print("You Entered Invalid1065 Marks.")
    exit()
if Score>=90:
    Grade = 'A'
elif Score>=80:
    Grade = 'B'
elif Score>=70:
    Grade = 'C'
elif Score>=60:
    Grade = 'D'
else:
    Grade = 'F'
print("You Achieved Grade is :",Grade)