try:
    n = int(input("숫자: "))
    print(f"10 / {n} = {10 / n}")
except ValueError:
    print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except Exception as e:
    print(f"기타 에러: {type(e).__name__}: {e}")
