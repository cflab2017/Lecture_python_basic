# 튜플
point = (10, 20)
x, y = point
print(x, y)

# 함수가 여러 값 반환할 때 튜플 활용
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)

# 한 개 짜리 튜플
single = (5,)
print(single, type(single))

# 튜플은 변경 불가
try:
    point[0] = 99
except TypeError as e:
    print("에러:", e)
