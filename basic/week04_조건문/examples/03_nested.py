age = int(input("나이: "))
has_ticket = input("티켓 있음(y/n): ") == "y"

if age >= 18:
    if has_ticket:
        print("입장 가능")
    else:
        print("티켓을 구매하세요")
else:
    print("미성년자는 입장 불가")
