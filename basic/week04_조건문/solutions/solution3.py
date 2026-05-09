import random

CHOICES = ["가위", "바위", "보"]
WIN = {"가위": "보", "바위": "가위", "보": "바위"}

user = input("선택(가위/바위/보): ")
if user not in CHOICES:
    print("잘못 입력했습니다")
else:
    com = random.choice(CHOICES)
    print(f"컴퓨터: {com}")
    if user == com:
        print("무승부")
    elif WIN[user] == com:
        print("사용자 승!")
    else:
        print("컴퓨터 승!")
