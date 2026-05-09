def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c1 = make_counter()
c2 = make_counter()  # 독립적인 카운터

print(c1(), c1(), c1())   # 1 2 3
print(c2())                # 1 (별도 카운터)

# 클로저로 함수 팩토리
def multiplier(factor):
    def mul(x):
        return x * factor
    return mul

double = multiplier(2)
triple = multiplier(3)
print(double(5), triple(5))   # 10 15
