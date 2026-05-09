# 의도적으로 에러를 발생시키는 예제
# 실행하면 ValueError 메시지가 나옵니다 — 정상입니다

print("'abc'를 정수로 변환 시도...")
try:
    int("abc")
except ValueError as e:
    print("에러 발생:", e)

print("'1.5'를 정수로 직접 변환 시도...")
try:
    int("1.5")
except ValueError as e:
    print("에러 발생:", e)
    print("이 경우는 float() 후 int() 로 두 번 변환:")
    print(int(float("1.5")))   # 1
