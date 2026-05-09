def greet(name, greeting="안녕"):
    return f"{greeting}, {name}님!"

print(greet("길동"))
print(greet("Alice", "Hello"))

# 키워드 인수
def make_user(name, age, city):
    return {"name": name, "age": age, "city": city}

u1 = make_user("홍길동", 20, "서울")
u2 = make_user(city="부산", name="김영희", age=25)
print(u1)
print(u2)
