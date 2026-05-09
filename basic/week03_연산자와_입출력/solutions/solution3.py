RATE = 1300  # 1 USD = 1300 KRW

krw = float(input("원화: "))
usd = krw / RATE

print(f"달러: ${usd:.2f}")
print(f"역변환 검증: ${usd:.2f} = {usd * RATE:,.0f}원")
