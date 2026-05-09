words = ["apple", "banana", "apple", "cherry", "date", "banana"]

length_map = {w: len(w) for w in set(words)}
print(length_map)

# 입력 순서 유지 버전
length_map2 = {}
for w in words:
    length_map2.setdefault(w, len(w))
print(length_map2)
