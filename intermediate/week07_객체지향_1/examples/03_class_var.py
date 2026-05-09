class Counter:
    total = 0   # 클래스 변수

    def __init__(self):
        Counter.total += 1
        self.id = Counter.total   # 인스턴스 변수

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(c1.id, c2.id, c3.id)   # 1 2 3
print(Counter.total)         # 3

# 위험한 패턴 — 클래스 변수에 리스트
class Bag:
    items = []

b1 = Bag()
b2 = Bag()
b1.items.append("apple")
print(b2.items)   # ['apple'] — b2도 같이 보임!

# 올바른 패턴
class Bag2:
    def __init__(self):
        self.items = []

b3 = Bag2()
b4 = Bag2()
b3.items.append("apple")
print(b4.items)   # []
