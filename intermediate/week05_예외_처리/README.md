# 5주차. 예외 처리

> 단계: 중급 | 선수: 4주차

## 학습 목표
- `try/except/else/finally` 의 각 절을 안다
- 예외 종류를 구분해 처리한다
- 사용자 정의 예외를 만든다
- 예외를 의도적으로 발생시킨다(`raise`)

## 1. 예외란

실행 중 발생하는 오류. 처리하지 않으면 프로그램이 종료됨.

```python
print(10 / 0)         # ZeroDivisionError
print(int("abc"))     # ValueError
print([1,2][5])       # IndexError
```

## 2. try / except

```python
try:
    n = int(input("숫자: "))
    print(10 / n)
except ValueError:
    print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except Exception as e:
    print(f"기타 에러: {e}")
```

## 3. else / finally

- `else`: try가 예외 없이 끝났을 때
- `finally`: 예외 여부와 무관하게 항상 실행 (정리 작업)

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("파일 없음")
else:
    print(f.read())
    f.close()
finally:
    print("정리 완료")
```

## 4. raise

예외를 의도적으로 발생.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("잔액 부족")
    return balance - amount
```

## 5. 사용자 정의 예외

`Exception` 상속.

```python
class InsufficientFundsError(Exception):
    pass

def transfer(account, amount):
    if account.balance < amount:
        raise InsufficientFundsError(f"잔액 {account.balance} < 요청 {amount}")
```

## 6. 예외 체인

기존 예외를 감싸서 새 예외 발생.

```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("입력 처리 실패") from e
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_try_except.py` | 기본 try/except |
| `02_else_finally.py` | else, finally |
| `03_raise.py` | raise 와 검증 |
| `04_custom.py` | 사용자 정의 예외 |

## ⚠️ 자주 하는 실수

1. **너무 광범위한 except**
   ```python
   try:
       ...
   except:           # 모든 예외 (KeyboardInterrupt 까지) — 위험
       pass
   ```
   → 가능한 좁은 예외 클래스 명시.

2. **`except ... as e: pass`** — 에러를 숨김. 최소한 로그라도.

3. **`finally` 에서 return** — try의 return 값을 덮어쓸 수 있음.

4. **except 순서** — 좁은 예외(`FileNotFoundError`)를 먼저, 넓은 것(`OSError`)을 뒤에.

## ❓ FAQ

**Q1. 모든 함수에 try를 둘러싸야 하나요?**
A. 아닙니다. **회복할 수 있는 곳에서만**. 보통 사용자 입력, 파일 I/O, 네트워크 호출.

**Q2. `Exception` 과 `BaseException` 의 차이?**
A. `BaseException` 이 최상위. `KeyboardInterrupt`, `SystemExit` 도 포함. 일반적으로는 `Exception` 까지만 잡음.

**Q3. 예외 vs 반환값 (None / -1)?**
A. 예외는 "정상 흐름이 아님" 을 명확히. 검색에서 "없음" 같은 정상 상황은 None 권장.

## 📝 과제 (exercises/)

- `exercise1.md` — 안전한 정수 입력 (`read_int`)
- `exercise2.md` — 사용자 정의 예외 (`InvalidScoreError`)
- `exercise3.md` — 파일 읽기 예외 처리

## 다음 주차

[6주차. 파일 입출력](../week06_파일_입출력/)
