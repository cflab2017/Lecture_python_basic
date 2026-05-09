import re

# 치환
print(re.sub(r"\d+", "?", "방 5개, 침대 3개"))

# 함수로 치환
def double(m):
    return str(int(m.group()) * 2)

print(re.sub(r"\d+", double, "방 5개, 침대 3개"))   # 방 10개, 침대 6개

# 컴파일 — 같은 패턴 여러 번 쓸 때
email_re = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
print(email_re.findall("a@b.com / hong@example.co.kr / not_an_email"))
