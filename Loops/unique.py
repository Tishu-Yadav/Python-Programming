'''List Uniqueness Checker
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]'''
items = ["apple", "banana", "orange", "apple", "mango"]
for i in items:
    if items.count(i) > 1:
        print("First Duplicate item is :", i)
        break