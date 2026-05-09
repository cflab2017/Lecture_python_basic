class InsufficientFundsError(Exception):
    """잔액 부족 시 발생"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"{self.owner}: 잔액 {self.balance} < 요청 {amount}"
            )
        self.balance -= amount

a = Account("홍길동", 1000)
a.withdraw(300)
print(a.balance)

try:
    a.withdraw(5000)
except InsufficientFundsError as e:
    print("커스텀 예외:", e)
