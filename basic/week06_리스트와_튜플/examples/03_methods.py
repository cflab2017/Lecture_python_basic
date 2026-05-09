nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.append(10)
print("append:", nums)

nums.insert(0, 0)
print("insert:", nums)

last = nums.pop()
print("pop:", last, nums)

nums.remove(1)
print("remove(1):", nums)

nums.sort()
print("sort:", nums)

nums.reverse()
print("reverse:", nums)

print("count(2):", nums.count(2))
print("index(5):", nums.index(5))
