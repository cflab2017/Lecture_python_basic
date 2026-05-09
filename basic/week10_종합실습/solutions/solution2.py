"""최종 과제 2 — 단어장 퀴즈 해답"""
import random

WORDS = {
    "apple": "사과", "book": "책", "table": "탁자", "door": "문",
    "water": "물", "fire": "불", "tree": "나무", "sky": "하늘",
    "love": "사랑", "time": "시간",
}

QUESTIONS = 10
score = 0

for i in range(1, QUESTIONS + 1):
    word, meaning = random.choice(list(WORDS.items()))
    answer = input(f"[{i}/{QUESTIONS}] {word}의 뜻은? ").strip()
    if answer == meaning:
        print("정답!")
        score += 1
    else:
        print(f"오답. 정답: {meaning}")

print(f"\n총점: {score} / {QUESTIONS}")
