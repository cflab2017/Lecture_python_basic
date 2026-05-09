def add(a, b):
    return a + b

def factorial(n):
    if n < 0:
        raise ValueError("음수는 안 됨")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
