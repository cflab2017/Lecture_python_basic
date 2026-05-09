data = ["a", "b", "a", "c", "b", "d"]

# 방법 1: 순회하며 수동 처리
seen = set()
result = []
for x in data:
    if x not in seen:
        seen.add(x)
        result.append(x)
print(f"방법 1: {result}")

# 방법 2: dict.fromkeys 사용 (Python 3.7+)
result2 = list(dict.fromkeys(data))
print(f"방법 2: {result2}")
