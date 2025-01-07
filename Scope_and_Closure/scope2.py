def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()

def g1():
    y = 70
    def g2():
        print(y)
    return g2
myresult = g1()
myresult()