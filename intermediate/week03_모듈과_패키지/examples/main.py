import calc
print(calc.add(3, 5))

from calc import sub, mul
print(sub(10, 4))
print(mul(6, 7))

from calc import add as plus
print(plus(100, 200))
