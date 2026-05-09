nums = [1, 2, 3, 4, 5]
print(f"원본: {nums}")

reversed1 = nums[::-1]   # 새 리스트
print(f"방법 1 (슬라이싱): {reversed1}")

nums.reverse()           # 제자리
print(f"방법 2 (reverse): {nums}")
print(f"원본도 변경됨: {nums}")
