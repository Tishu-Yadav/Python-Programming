'''Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.'''
word = input("Enter a Word :")
for char in word:
    count = word.count(char)
    if count == 1:
        print("First Non-Repeated Char is :",char)
        break
