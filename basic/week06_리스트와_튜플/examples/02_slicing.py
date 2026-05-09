nums = [10, 20, 30, 40, 50]

print(nums[1:4])      # [20, 30, 40]
print(nums[:3])       # [10, 20, 30]
print(nums[2:])       # [30, 40, 50]
print(nums[::-1])     # [50, 40, 30, 20, 10]
print(nums[::2])      # [10, 30, 50]

# 문자열도 슬라이싱 가능
s = "Hello"
print(s[1:4])         # ell
print(s[::-1])        # olleH
