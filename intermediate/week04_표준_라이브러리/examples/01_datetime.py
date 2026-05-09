from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%Y년 %m월 %d일 %A"))

today = date.today()
birthday = date(2000, 5, 9)
delta = today - birthday
print(f"태어난 지 {delta.days}일")

next_week = now + timedelta(days=7)
print(f"다음 주: {next_week.strftime('%Y-%m-%d')}")

# 문자열을 datetime으로 파싱
parsed = datetime.strptime("2026-05-09 14:30", "%Y-%m-%d %H:%M")
print(parsed)
