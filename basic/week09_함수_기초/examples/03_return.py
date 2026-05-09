def square(x):
    return x * x

def min_max(nums):
    return min(nums), max(nums)

print(square(5))

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(f"최소 {lo}, 최대 {hi}")

# return 없으면 None
def show(x):
    print(x)

y = show(10)
print(f"y = {y}")
