# 기본
squares = [x * x for x in range(10)]
print(squares)

# 조건 필터
even_sq = [x * x for x in range(10) if x % 2 == 0]
print(even_sq)

# 중첩
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
print(pairs)

# 문자열 처리
words = ["Hello", "World", "Python"]
upper = [w.upper() for w in words]
print(upper)
