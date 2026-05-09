import random

print(random.random())
print(random.randint(1, 100))
print(random.choice(["가위", "바위", "보"]))
print(random.sample(range(1, 46), 6))

# 시드 고정 → 재현 가능
random.seed(42)
print([random.randint(1, 10) for _ in range(5)])

# 리스트 섞기 (제자리)
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)

# 가중치 선택
result = random.choices(["A", "B", "C"], weights=[5, 3, 1], k=10)
print(result)
