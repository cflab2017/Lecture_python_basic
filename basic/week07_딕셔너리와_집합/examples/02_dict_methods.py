d = {"a": 1, "b": 2, "c": 3}

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

# get: 안전 조회
print(d.get("z"))
print(d.get("z", "없음"))

# in
print("a" in d)
print("z" in d)

# 순회
for key, value in d.items():
    print(f"{key} = {value}")
