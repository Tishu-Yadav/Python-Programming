def tishu(num):
    def yadav(x):
        return x**num
    return yadav # it return the definition of function yadav as well refernce of those variables which are used in function. 
g = tishu(3)
f = tishu(2)
print(g)
print(g(3))
print(f(3))