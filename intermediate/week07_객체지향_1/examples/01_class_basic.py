class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액 부족")
        self.balance -= amount

a = Account("홍길동", 1000)
a.deposit(500)
print(a.balance)
a.withdraw(300)
print(a.balance)

b = Account("김영희")  # balance 기본값 0
b.deposit(100)
print(b.balance)
