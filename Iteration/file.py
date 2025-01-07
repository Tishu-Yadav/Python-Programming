f = open('Iteration/script.py')
print(f.readline()) 
print(f.readline()) 
print(f.readline()) 
print(f.readline()) 
print(f.readline()) 
for line in open('Iteration/script.py'):
    print(line,end="")
#print(f.__next__())
if iter(f) is f:
    print("\nTrue")
#list =[1,2,3,4]
#I = iter(list)
#I.__next__() raise exception of Stop Iteration when complete list is iterated.