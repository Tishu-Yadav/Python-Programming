'''Fruit Ripeness Checker
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)'''
Fruit = 'Banana'
Colour = 'Green'

if Colour == 'Green':
     State = 'Unripe'
elif Colour == 'Yellow':
     State ='Ripe'
elif Colour == 'Brown':
     State = 'Overripe'
print("Your Fruit",Fruit,"is",State)