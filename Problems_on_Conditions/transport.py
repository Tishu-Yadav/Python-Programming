'''Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).'''
Distance = int(input("Enter Exact Distance:"))
if Distance < 3:
    mode = 'Walk'
elif Distance <= 15:
    mode = 'Bike'
else:
    mode = 'Car'
print("AI Recommend You",mode,"for",Distance,"KM Distance")