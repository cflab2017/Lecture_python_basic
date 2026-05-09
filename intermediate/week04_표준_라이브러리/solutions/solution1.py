from datetime import date

target = input("목표일(YYYY-MM-DD): ").strip()
y, m, d = map(int, target.split("-"))
target_date = date(y, m, d)
today = date.today()

delta = (target_date - today).days
print(f"오늘: {today}")
if delta > 0:
    print(f"목표일까지 D-{delta}")
elif delta < 0:
    print(f"목표일에서 D+{-delta}")
else:
    print("D-DAY!")
