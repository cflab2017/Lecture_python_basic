def f():
    x = 10  # 지역
    print(f"안에서: x = {x}")

f()
# print(x)  # NameError

# global 키워드
total = 0

def add_to_total(n):
    global total
    total += n

add_to_total(10)
add_to_total(20)
print(f"total = {total}")
