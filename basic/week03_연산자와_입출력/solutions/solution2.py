price = int(input("결제 금액: "))
paid = int(input("받은 금액: "))

change = paid - price
print(f"거스름돈: {change:,}원")
