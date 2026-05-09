"""CLI 계산기 — 메뉴형 + 결과 누적"""

OPS = {
    "1": ("+", lambda a, b: a + b),
    "2": ("-", lambda a, b: a - b),
    "3": ("*", lambda a, b: a * b),
    "4": ("/", lambda a, b: a / b if b != 0 else None),
}

def main():
    history = []
    last = None
    while True:
        print("\n[메뉴] 1.+ 2.- 3.* 4./ 5.이전결과 사용 6.종료")
        choice = input("선택: ").strip()
        if choice == "6":
            break
        if choice not in OPS:
            print("잘못된 선택"); continue
        try:
            if last is not None and input(f"첫 번째 수 (이전 결과 {last}): ").strip() == "":
                a = last
            else:
                a = float(input("첫 번째 수: "))
            b = float(input("두 번째 수: "))
        except ValueError:
            print("숫자만 입력"); continue

        symbol, fn = OPS[choice]
        result = fn(a, b)
        if result is None:
            print("0으로 나눌 수 없습니다")
            continue
        print(f"결과: {a} {symbol} {b} = {result}")
        history.append(f"{a} {symbol} {b} = {result}")
        last = result

    print("\n[연산 이력]")
    for h in history:
        print(f"  {h}")

if __name__ == "__main__":
    main()
