'''Weather Activity Suggestion
Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).'''
Weather = 'Snowy'
if Weather == 'Sunny':
    Activity = "Go for a Walk"
elif Weather == 'Rainy':
    Activity = "Read a Book"
elif Weather == 'Snowy':
    Activity = "Build a snowman"
print("Weather is",Weather,"so you",Activity)