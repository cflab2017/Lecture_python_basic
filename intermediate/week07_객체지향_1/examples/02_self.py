class Greeter:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hi, I'm {self.name}"

g = Greeter("Alice")
print(g.hello())            # Hi, I'm Alice

# 위 호출은 사실 아래와 동일
print(Greeter.hello(g))     # Hi, I'm Alice
