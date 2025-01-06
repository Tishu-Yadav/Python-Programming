"""Movie Ticket Pricing
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday."""
Age = int(input("Enter Your Age :"))
Day = input("Enter Day:")
A = Day.title()
Price = 12 if Age>=18 else 8

if A == "Wednesday":
    Price = Price-2
print("Your Ticket Price is:$",Price)