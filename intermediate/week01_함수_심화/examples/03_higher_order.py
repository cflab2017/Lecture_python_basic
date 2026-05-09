nums = [1, 2, 3, 4, 5]

# map: 모든 원소를 변환
squared = list(map(lambda x: x * x, nums))
print(squared)

# filter: 조건에 맞는 것만
odds = list(filter(lambda x: x % 2, nums))
print(odds)

# sorted with key
people = [("Alice", 30), ("Bob", 25), ("Charlie", 28)]

by_age = sorted(people, key=lambda p: p[1])
print(by_age)

by_name = sorted(people, key=lambda p: p[0])
print(by_name)

# 내림차순
by_age_desc = sorted(people, key=lambda p: p[1], reverse=True)
print(by_age_desc)
