s = input("문자열: ")
cleaned = s.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("회문입니다")
else:
    print("회문이 아닙니다")
