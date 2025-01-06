Food = ("Burger","Pizza","Chocolate")
print(Food)
print(type(Food))
print(Food[1],Food[:])
more_food = ("Milk","Vegetable")
All_Food = Food + more_food
print(more_food)
print(All_Food)
print(All_Food.count("Burger"))
print(len(All_Food))
if "Burger" in Food:
    print("yummy")
