class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금은 양수")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("출금은 양수")
        if amount > self.balance:
            raise ValueError(f"잔액 부족: {self.balance} < {amount}")
        self.balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

a = BankAccount("Alice", 1000)
b = BankAccount("Bob")
a.transfer(b, 300)
print(a.balance, b.balance)
