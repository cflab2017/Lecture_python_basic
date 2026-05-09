"""가위바위보 — 3판 2선승 + 통산 전적"""
import random

CHOICES = ["가위", "바위", "보"]
SHORT = {"r": "가위", "p": "바위", "s": "보"}
WIN = {"가위": "보", "바위": "가위", "보": "바위"}

def get_user_choice():
    while True:
        raw = input("선택(가위/바위/보 또는 r/p/s): ").strip().lower()
        if raw in CHOICES:
            return raw
        if raw in SHORT:
            return SHORT[raw]
        print("  ⚠️ 가위/바위/보 중 하나를 입력하세요")

def play_round(round_num, user_score, com_score):
    print(f"\n[{round_num}라운드]  현재 스코어 ({user_score} : {com_score})")
    user = get_user_choice()
    com = random.choice(CHOICES)
    print(f"컴퓨터: {com}", end="  ")
    if user == com:
        print("→ 무승부")
        return user_score, com_score
    if WIN[user] == com:
        print("→ 사용자 승!")
        return user_score + 1, com_score
    print("→ 컴퓨터 승!")
    return user_score, com_score + 1

def play_match():
    us = cs = 0
    r = 1
    while us < 3 and cs < 3:
        us, cs = play_round(r, us, cs)
        r += 1
    winner = "사용자" if us >= 3 else "컴퓨터"
    print(f"\n🏆 매치 승자: {winner} ({us}:{cs})")
    return winner

def main():
    user_wins = com_wins = ties = 0
    while True:
        winner = play_match()
        if winner == "사용자":
            user_wins += 1
        else:
            com_wins += 1
        if input("\n한 게임 더? (y/n): ").strip().lower() != "y":
            break
    print(f"\n[통산 전적]  사용자 {user_wins} 매치 승, 컴퓨터 {com_wins} 매치 승")

if __name__ == "__main__":
    main()
