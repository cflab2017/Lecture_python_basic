square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

# 람다는 보통 다른 함수의 인자로
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x > 2, nums)))
