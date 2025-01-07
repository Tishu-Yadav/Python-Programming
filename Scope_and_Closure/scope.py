name = "Tishu"#global variable
def func():
    name = "Tribhuvan"#local Variable
    print(name)
print(name)
func()

x = 99
def func2(y):
    z = x + y
    return z
result = func2(75)
print(result)

def func3(y):
    global x
    x = 67
    z = x + y
    return z
add = func3(80)
print(add)