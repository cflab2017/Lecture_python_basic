words = ["apple", "banana", "cherry"]

# 딕셔너리 컴프리헨션
length_map = {w: len(w) for w in words}
print(length_map)

# 키-값 뒤집기
d = {"a": 1, "b": 2, "c": 3}
inv = {v: k for k, v in d.items()}
print(inv)

# 집합 컴프리헨션
unique_lens = {len(w) for w in words}
print(unique_lens)

text = "the quick brown fox jumps over the lazy dog"
unique_words = {w for w in text.split()}
print(len(unique_words))
