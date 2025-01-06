Food = ["Burger","Sweet","Vegetable","Chips"]
print(Food)
Food[3]="Tomato"
print(Food)
print(Food[1:3] , Food[0:])#Slicing.
for item in Food:
    print(item)

for item in Food:
    print(item,end="-")

if "Burger" in Food:
    print("Yummy")

Food.append("Sugar") # Insert a Element in the Last
print(Food)
Food.pop() # Removes a Element from Last
print(Food)
Food.remove("Sweet") #Removes a Specific Element From the List
print(Food)
Food.insert(1,"Sweet") # Insert Element at Specific Position
print(Food)
Food_Copy = Food.copy()
print(Food_Copy)
Food_Copy.append("Burfi")
print(Food_Copy)
squared_nums =[x**2 for x in range(10)]
print(squared_nums)