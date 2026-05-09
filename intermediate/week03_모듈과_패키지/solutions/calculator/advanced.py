import math

def power(base, exp):
    return base ** exp

def sqrt(x):
    if x < 0:
        raise ValueError("음수의 제곱근")
    return math.sqrt(x)
