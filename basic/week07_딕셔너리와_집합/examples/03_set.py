fruits = {"사과", "바나나", "포도"}
fruits.add("딸기")
fruits.discard("없는과일")  # 에러 안 남
print(fruits)

# 중복 제거
nums = [1, 2, 2, 3, 3, 3]
print(set(nums))   # {1, 2, 3}

# 집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("합집합:", a | b)
print("교집합:", a & b)
print("차집합:", a - b)
print("대칭차:", a ^ b)
