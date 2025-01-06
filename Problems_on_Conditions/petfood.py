'''Pet Food Recommendation
Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).'''
Age = int(input("Enter Age of Your Pet :"))
Name = input("Enter Name of Your Pet Dog or Cat:").title()

if (Age < 2 and Name == "Dog"):
    print("AI Recommend You for Your ",Name,"Puppy Food")
elif (Age > 5 and Name == "Cat"):
    print("AI Recommend You for Your ",Name,"Senior Cat Food")
else:
    print("Invalid Age or Pet")