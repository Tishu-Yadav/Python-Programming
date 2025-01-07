'''Reverse a String
Problem: Reverse a string using a loop.'''
word = input("Enter a Word or String:")
reverse = ""
for char in word:
    reverse = char + reverse
print("Your Given Word",word,"in reverse form is:",reverse)