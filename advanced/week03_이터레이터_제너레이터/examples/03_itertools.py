import itertools as it

# count + islice
counter = it.count(1, 2)
print(list(it.islice(counter, 5)))   # [1, 3, 5, 7, 9]

# combinations
print(list(it.combinations([1, 2, 3, 4], 2)))

# permutations
print(list(it.permutations([1, 2, 3], 2)))

# groupby (정렬된 데이터 필요)
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)]
data.sort(key=lambda x: x[0])
for key, group in it.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# product (사전 곱)
print(list(it.product([1, 2], "ab")))

# accumulate
print(list(it.accumulate([1, 2, 3, 4, 5])))
