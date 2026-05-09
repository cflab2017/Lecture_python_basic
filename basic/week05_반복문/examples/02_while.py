# 1~5 출력
n = 1
while n <= 5:
    print(n, end=" ")
    n += 1
print()

# 사용자 입력으로 종료
while True:
    cmd = input("명령(quit으로 종료): ")
    if cmd == "quit":
        print("종료합니다")
        break
    print(f"실행: {cmd}")
