Animals = {"Milk":"Cow","Race":"Horse","King":"Lion"}
print(Animals)
print(Animals["Milk"])
print(Animals.get("Race"))
print(Animals.get("Water"))
Animals["Water"]="Fish"
for animal in Animals:
    print(animal)

for animal in Animals:
    print(animal,Animals[animal])

for key,value in Animals.items():
    print(key,"-",value)

if "Milk" in Animals:
    print("Drink")

print(len(Animals))

print(Animals.pop("Milk"))
print(Animals.popitem())
del Animals["Race"]
Animals_copy = Animals.copy()
print(Animals_copy)

nested = {"Colour":{"Black":"Dark","White":"Light"},"Taste":{"Burger":"Yummy","Pizza":"Spicy"}}
print(nested)

cube_nums = {x : x**3 for x in range(10)}
print(cube_nums)
print(cube_nums.clear())

Type = ["Black","Red","White"]
Value = "Colour"

new_dict = dict.fromkeys(Type,Value)
print(new_dict)

new_dict1 = dict.fromkeys(Type,Type)
print(new_dict1)
