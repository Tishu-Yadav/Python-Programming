"""Age Group Categorization
Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+)."""
Age = int(input("Enter Your Age :"))

if Age<13:
    print("You are Child.")
elif Age<20:
    print("You are Teenager")
elif Age<60:
    print("You are Adult")
else:
    print("You are Senior")