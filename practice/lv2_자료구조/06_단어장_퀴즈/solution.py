"""단어장 퀴즈 — 양방향 + 복습 모드"""
import random

WORDS = {
    "apple": "사과", "book": "책", "table": "탁자", "door": "문",
    "water": "물", "fire": "불", "tree": "나무", "sky": "하늘",
    "love": "사랑", "time": "시간", "house": "집", "car": "자동차",
}

def quiz(pairs, mode):
    score = 0
    wrong = []
    for i, (en, ko) in enumerate(pairs, 1):
        if mode == "en2ko":
            q, a = en, ko
        elif mode == "ko2en":
            q, a = ko, en
        else:  # random
            if random.random() < 0.5:
                q, a = en, ko
            else:
                q, a = ko, en
        ans = input(f"[{i}/{len(pairs)}] {q}? ").strip()
        if ans == a:
            print("✓ 정답")
            score += 1
        else:
            print(f"✗ 오답 (정답: {a})")
            wrong.append((q, a))
    return score, wrong

def main():
    print("[모드] 1.영→한 2.한→영 3.랜덤")
    mode_map = {"1": "en2ko", "2": "ko2en", "3": "random"}
    mode = mode_map.get(input("선택: ").strip(), "en2ko")

    pairs = random.sample(list(WORDS.items()), min(10, len(WORDS)))
    score, wrong = quiz(pairs, mode)
    print(f"\n총점: {score} / {len(pairs)}")

    if wrong and input("\n틀린 문제만 복습? (y/n): ").strip().lower() == "y":
        score2, _ = quiz(wrong, mode)
        print(f"복습 점수: {score2} / {len(wrong)}")

if __name__ == "__main__":
    main()
