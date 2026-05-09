import itertools as it

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(it.islice(fib(), 20)))
