# 과제 1. BankAccount 클래스

## 요구사항
- 속성: `owner`, `balance`
- 메서드:
  - `__init__(owner, balance=0)`
  - `deposit(amount)` — 양수만 허용
  - `withdraw(amount)` — 잔액 부족 시 예외
  - `transfer(other_account, amount)` — 다른 계좌로 송금
- 모든 검증 실패는 `ValueError` 로

## 사용 예
```python
a = BankAccount("Alice", 1000)
b = BankAccount("Bob")
a.transfer(b, 300)
print(a.balance, b.balance)   # 700 300
```
