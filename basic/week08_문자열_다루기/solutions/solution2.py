email = input("이메일: ").strip()

if " " in email:
    print("잘못된 형식")
elif email.count("@") != 1:
    print("잘못된 형식")
else:
    local, _, domain = email.partition("@")
    if "." not in domain or not local or not domain:
        print("잘못된 형식")
    else:
        print("유효한 이메일")
