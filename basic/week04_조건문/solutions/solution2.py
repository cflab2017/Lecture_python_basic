year = int(input("연도: "))

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

label = "윤년" if is_leap else "평년"
print(f"{year}년은 {label}입니다.")
