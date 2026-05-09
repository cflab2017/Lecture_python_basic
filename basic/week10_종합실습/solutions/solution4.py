"""최종 과제 4 — 숫자 야구 해답"""
import random

# 0~9 중 중복 없는 3자리 숫자
digits = random.sample(range(10), 3)
answer = "".join(str(d) for d in digits)
tries = 0

print("3자리 숫자 야구 시작! (중복 없음)")
while True:
    guess = input("숫자 입력 (3자리): ").strip()
    if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
        print("3자리 중복 없는 숫자만 입력")
        continue
    tries += 1
    strike = sum(1 for i in range(3) if guess[i] == answer[i])
    ball = sum(1 for i in range(3) if guess[i] in answer and guess[i] != answer[i])
    if strike == 3:
        print(f"3 스트라이크! 정답입니다 (시도 {tries}회)")
        break
    print(f"{strike} 스트라이크 {ball} 볼")
