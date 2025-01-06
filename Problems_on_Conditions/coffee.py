'''Coffee Customization
Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.'''
Order = 'Medium'
Extra_Shot = input("Enter True or False for Extra Shot:").title()
if Extra_Shot == "True":
    Coffee = Order + " with Extra Shot of a Coffee"
else:
    Coffee = Order + " Coffee"

print("You Ordered",Coffee)

