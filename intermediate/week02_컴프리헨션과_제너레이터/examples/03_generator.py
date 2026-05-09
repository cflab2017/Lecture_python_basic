def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for x in fib(10):
    print(x, end=" ")
print()

# list로 한 번에 받기
print(list(fib(10)))

# 무한 제너레이터
def naturals():
    n = 1
    while True:
        yield n
        n += 1

import itertools
first_5 = list(itertools.islice(naturals(), 5))
print(first_5)
