def stats(*nums):
    if not nums:
        return (0, 0)
    avg = sum(nums) / len(nums)
    var = sum((x - avg) ** 2 for x in nums) / len(nums)
    return (avg, var)

print(stats(1, 2, 3, 4, 5))
print(stats())
print(stats(10, 20, 30))
