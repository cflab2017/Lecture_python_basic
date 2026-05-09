"""숫자 맞추기 — 난이도 선택 + 시도 제한"""
import random

LEVELS = {
    "1": ("쉬움", 1, 50, 7),
    "2": ("보통", 1, 100, 7),
    "3": ("어려움", 1, 500, 10),
}

def pick_difficulty():
    while True:
        choice = input("난이도 (1.쉬움 2.보통 3.어려움): ").strip()
        if choice in LEVELS:
            return LEVELS[choice]
        print("1, 2, 3 중에서 선택")

def play_round(low, high, max_tries):
    answer = random.randint(low, high)
    print(f"{low}~{high}, {max_tries}번 안에 맞춰보세요")
    for left in range(max_tries, 0, -1):
        try:
            guess = int(input(f"[남은 {left}회] 숫자: "))
        except ValueError:
            print("  숫자만 입력")
            continue
        if guess < answer:
            print("  → 더 큰 수")
        elif guess > answer:
            print("  → 더 작은 수")
        else:
            print(f"  ✓ 정답! (시도 {max_tries - left + 1}회)")
            return True
    print(f"  횟수 초과! 정답은 {answer}")
    return False

def main():
    while True:
        name, low, high, tries = pick_difficulty()
        print(f"\n[{name}]")
        play_round(low, high, tries)
        if input("\n한 번 더? (y/n): ").strip().lower() != "y":
            break

if __name__ == "__main__":
    main()
