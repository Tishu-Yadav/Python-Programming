'''Password Strength Checker
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).'''
Password = input("Enter Your Password:")
Length = len(Password)
if Length < 6:
    strength = "Weak"
elif Length <=10 :
    strength = "Medium"
else:
    strength = "Strong"

print("Your Password Strength is",strength)