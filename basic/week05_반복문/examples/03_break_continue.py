# 1~10 중 5는 건너뛰고, 8에서 종료
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i, end=" ")
print()
# 출력: 1 2 3 4 6 7

# 첫 번째 짝수만 찾기
for n in [3, 7, 11, 4, 9]:
    if n % 2 == 0:
        print(f"첫 번째 짝수: {n}")
        break
