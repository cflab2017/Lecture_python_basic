class Account:
    def __init__(self, owner, balance):
        self._owner = owner       # 내부용 (관례)
        self.__balance = balance  # name mangled

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("금액은 양수")
        self.__balance += amount

a = Account("홍길동", 1000)
print(a.get_balance())
print(a._owner)        # 가능 (관례로 자제)

try:
    print(a.__balance)
except AttributeError as e:
    print("막혔음:", e)

# 우회 가능 (권장 X)
print(a._Account__balance)
