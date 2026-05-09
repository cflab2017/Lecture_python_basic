# 0, "", [], None, False는 모두 거짓 처리
values = [0, "", [], None, False, 1, "hi", [1, 2], True]

for v in values:
    if v:
        print(f"{v!r:>10}: Truthy")
    else:
        print(f"{v!r:>10}: Falsy")
