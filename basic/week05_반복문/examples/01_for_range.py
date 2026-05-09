# 0부터 4까지
for i in range(5):
    print(i, end=" ")
print()

# 1부터 10까지
for i in range(1, 11):
    print(i, end=" ")
print()

# 0부터 10까지 2씩 증가
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 합계 구하기
total = 0
for i in range(1, 101):
    total += i
print(f"1~100 합계: {total}")
