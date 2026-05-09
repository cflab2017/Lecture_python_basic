# 2주차. 변수와 자료형

> 단계: 기초 | 선수: 1주차 (환경 설치, `print()`)

## 학습 목표
- 변수의 개념과 할당 문법을 이해한다
- 4가지 기본 자료형(`int`, `float`, `str`, `bool`)을 구분한다
- `type()` 으로 변수의 타입을 확인한다
- `int()`, `float()`, `str()` 으로 형 변환한다
- `None` 의 의미를 안다

## 1. 변수란

변수는 **값에 이름을 붙인 것**입니다. 메모리의 어떤 공간에 데이터를 저장하고, 그 공간을 이름으로 불러옵니다.

```python
age = 20         # age 라는 변수에 20을 담음
name = "홍길동"  # name 에 문자열을 담음
print(age)       # 20 출력
```

`=` 은 수학의 "같다"가 아니라 **할당(assign)** 입니다. 오른쪽 값을 왼쪽 변수에 넣는다는 뜻.

### 변수 명명 규칙
- 영문, 숫자, `_` 만 사용. 첫 글자는 숫자 불가
- 대소문자 구분 (`age` ≠ `Age`)
- `if`, `for` 같은 예약어는 못 씀
- 관례: **snake_case** (`user_name`, `total_score`)

## 2. 기본 자료형

| 타입 | 예시 | 설명 |
|------|------|------|
| `int` | `10`, `-3`, `0` | 정수 |
| `float` | `3.14`, `-0.5` | 실수 (소수) |
| `str` | `"hello"`, `'안녕'` | 문자열 (작은/큰따옴표 둘 다 가능) |
| `bool` | `True`, `False` | 참/거짓 (대문자 시작!) |
| `NoneType` | `None` | "값이 없음"을 나타냄 |

→ examples/01_variables.py, 02_types.py 참고.

## 3. 형 변환 (Type Casting)

타입을 강제로 바꿉니다. 입력 받은 값은 항상 문자열이라 숫자로 바꿔야 계산할 수 있습니다.

```python
num_str = "123"
num_int = int(num_str)
print(num_int + 7)   # 130
```

| 함수 | 설명 |
|------|------|
| `int(x)` | x를 정수로 변환 |
| `float(x)` | x를 실수로 변환 |
| `str(x)` | x를 문자열로 변환 |
| `bool(x)` | x를 불리언으로 변환 |

**불가능한 변환은 ValueError:**
```python
int("abc")     # ValueError: invalid literal for int() with base 10: 'abc'
```

## 4. type() 함수

```python
print(type(10))            # <class 'int'>
print(type(3.14))          # <class 'float'>
print(type("hi"))          # <class 'str'>
print(type(True))          # <class 'bool'>
print(type(None))          # <class 'NoneType'>
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_variables.py` | 변수 선언과 사용 |
| `02_types.py` | `type()` 으로 타입 확인 |
| `03_casting.py` | 정상 형 변환 |
| `04_casting_error.py` | 형 변환 실패 (의도적 에러) |

## ⚠️ 자주 하는 실수

1. **변수 이름을 숫자로 시작**
   ```python
   2nd_player = "Bob"  # SyntaxError
   ```
   → `second_player` 또는 `player2` 로 변경.

2. **`True`/`False` 를 소문자로**
   ```python
   is_ok = true   # NameError
   ```
   → 첫 글자 대문자: `True`, `False`, `None`.

3. **문자열에 따옴표 빠짐**
   ```python
   name = 홍길동   # NameError: name '홍길동' is not defined
   ```
   → `name = "홍길동"` 처럼 따옴표로 감싸야 문자열.

4. **정수/문자열 혼합 더하기**
   ```python
   age = 20
   print("나이: " + age)   # TypeError
   ```
   → `print("나이: " + str(age))` 또는 f-string `f"나이: {age}"`.

5. **`input()` 결과를 그대로 계산**
   ```python
   n = input("숫자: ")   # 항상 문자열!
   print(n + 1)          # TypeError
   ```
   → `n = int(input("숫자: "))` 로 변환.

## ❓ 자주 묻는 질문 (FAQ)

**Q1. `'`(작은따옴표)와 `"`(큰따옴표)는 차이가 있나요?**
A. 기능적으로 동일합니다. 다만 문자열 안에 따옴표를 넣고 싶을 때 다른 종류를 사용하면 편합니다 (`"It's me"`).

**Q2. 변수에는 어떤 타입이든 다시 할당할 수 있나요?**
A. 네. 파이썬은 동적 타입 언어라 `x = 10` 한 뒤 `x = "hello"` 해도 됩니다. 다만 가독성 때문에 권장하지 않습니다.

**Q3. `0` 과 `False` 는 같은가요?**
A. 비교(`==`)하면 True지만, 타입은 다릅니다. `int` vs `bool`. 자세한 동등성은 추후 학습.

**Q4. 숫자에 콤마를 넣어도 되나요? (`1,000,000`)**
A. 안 됩니다. 콤마 대신 언더스코어 사용 가능: `1_000_000` (가독성용).

## 📝 과제 (exercises/)

- `exercise1.md` — 만 나이 계산기
- `exercise2.md` — 5개 변수 + 타입 출력
- `exercise3.md` — 4가지 자료형 모두 사용하는 짧은 프로그램

## 정답 (solutions/)

먼저 직접 풀어보고 막힐 때만 참고.

## 다음 주차

[3주차. 연산자와 입출력](../week03_연산자와_입출력/) — 사용자 입력 받기와 사칙연산
