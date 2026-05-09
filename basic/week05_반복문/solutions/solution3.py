import random

answer = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("숫자 입력: "))
    tries += 1
    if guess < answer:
        print("더 큰 수입니다.")
    elif guess > answer:
        print("더 작은 수입니다.")
    else:
        print(f"정답! 시도 횟수: {tries}")
        break
