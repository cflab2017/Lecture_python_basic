name = "Alice"
score = 92.345
price = 1234567

print(f"{name:<10}|")    # 좌측 정렬
print(f"{name:>10}|")    # 우측 정렬
print(f"{name:^10}|")    # 가운데
print(f"{name:*^10}|")   # 가운데, 채움 *

print(f"{score:.2f}")    # 92.35
print(f"{price:,}")      # 1,234,567
print(f"{0.85:.0%}")     # 85%
print(f"{255:b}")        # 11111111 (2진수)
print(f"{255:x}")        # ff (16진수)

# 표 형식
data = [("Alice", 92), ("Bob", 78), ("Charlie", 100)]
for n, s in data:
    print(f"{n:<10}{s:>5}점")
