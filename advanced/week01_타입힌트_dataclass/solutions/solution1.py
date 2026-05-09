"""중급 7주차 BankAccount 에 타입 힌트 추가"""

class BankAccount:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("입금은 양수")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("출금은 양수")
        if amount > self.balance:
            raise ValueError(f"잔액 부족: {self.balance} < {amount}")
        self.balance -= amount

    def transfer(self, other: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        other.deposit(amount)

a = BankAccount("Alice", 1000)
b = BankAccount("Bob")
a.transfer(b, 300)
print(a.balance, b.balance)
