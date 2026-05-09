name = "홍길동"
score = 95
price = 12345

print(f"{name}님의 점수는 {score}점입니다")
print(f"가격: {price:,}원")             # 12,345원
print(f"원주율: {3.141592:.2f}")         # 3.14
print(f"이름: {name:>10}")               # 우측정렬 폭 10
print(f"이름: {name:<10}|")              # 좌측정렬
print(f"이름: {name:^10}|")              # 가운데정렬
