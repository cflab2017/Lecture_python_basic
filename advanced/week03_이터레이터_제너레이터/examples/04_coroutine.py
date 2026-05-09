def echo():
    while True:
        x = yield
        print(f"받음: {x}")

co = echo()
next(co)                # 첫 yield 까지 진행
co.send("hello")
co.send("world")
co.close()

# 상태가 있는 누적기
def averager():
    total = 0
    count = 0
    avg = None
    while True:
        x = yield avg
        total += x
        count += 1
        avg = total / count

a = averager()
next(a)
print(a.send(10))   # 10.0
print(a.send(20))   # 15.0
print(a.send(30))   # 20.0
