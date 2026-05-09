def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c1 = make_counter()
c2 = make_counter()
print(c1(), c1(), c1())   # 1 2 3
print(c2())               # 1
print(c1())               # 4
