import math # for math libraries.
import random # for random numbers.
from decimal import Decimal # for handling Decimal numbers.
from fractions import Fraction # for handling fraction Numbers.
a = math.floor(3.5) # Give smallest integer value which is nearest
print(a)
b = math.floor(-3.5)
print(b)
c=math.trunc(3.5) # Give nearest Integer Value Towards Zero
d = hex(64) # Convert into hexadecimal
print(d)
e = oct(64)
f = bin(64)
print(e,f)
g = random.random()
h = random.randint(1,100)
print(g,h)
i = Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
print(i)
myfra = Fraction(2,7)
print(myfra)
j = type(True)
print(j)
k = True + 5
print(k)

