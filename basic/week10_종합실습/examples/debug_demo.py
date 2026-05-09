"""print 디버깅과 간단한 try-except 맛보기"""

def divide(a, b):
    print(f"DEBUG: divide 호출 a={a}, b={b}")
    try:
        result = a / b
    except ZeroDivisionError:
        print("ERROR: 0으로 나눌 수 없습니다")
        return None
    print(f"DEBUG: 결과 {result}")
    return result

print(divide(10, 2))
print(divide(10, 0))
print(divide(7, 3))
