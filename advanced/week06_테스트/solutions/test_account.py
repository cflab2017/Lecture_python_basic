"""pytest test_account.py 로 실행"""
import pytest

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금은 양수")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액 부족")
        self.balance -= amount

@pytest.fixture
def account():
    return BankAccount("Alice", 1000)

def test_initial_balance(account):
    assert account.balance == 1000

def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700

def test_deposit_negative_raises(account):
    with pytest.raises(ValueError, match="양수"):
        account.deposit(-10)

def test_withdraw_overdraft(account):
    with pytest.raises(ValueError, match="부족"):
        account.withdraw(2000)
