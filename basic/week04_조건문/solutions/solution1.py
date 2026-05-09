score = int(input("점수: "))

if score < 0 or score > 100:
    print("잘못된 점수")
elif score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
elif score >= 60:
    print("학점: D")
else:
    print("학점: F")
