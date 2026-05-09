def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        return None
    return a / b

while True:
    print("\n[메뉴] 1.+ 2.- 3.* 4./ 5.종료")
    choice = input("선택: ").strip()
    if choice == "5":
        break
    if choice not in {"1", "2", "3", "4"}:
        print("잘못된 선택")
        continue
    a = float(input("첫 번째 수: "))
    b = float(input("두 번째 수: "))
    funcs = {"1": add, "2": sub, "3": mul, "4": div}
    result = funcs[choice](a, b)
    if result is None:
        print("0으로 나눌 수 없습니다")
    else:
        print(f"결과: {result}")
