"""Function with *args
Problem: Write a function that takes variable number of arguments and returns their sum."""
def sum(*args):
    add = 0
    print(args)
    for i in args:
        add = add + i
    return add
print(sum(1,2,3,4))
print(sum(6,7,8,9,5,7,4))