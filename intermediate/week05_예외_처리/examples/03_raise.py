def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("금액은 양수여야 합니다")
    if amount > balance:
        raise ValueError(f"잔액 부족: {balance} < {amount}")
    return balance - amount

print(withdraw(1000, 300))

try:
    withdraw(1000, -10)
except ValueError as e:
    print("실패:", e)

try:
    withdraw(1000, 5000)
except ValueError as e:
    print("실패:", e)
