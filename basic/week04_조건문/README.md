# 4주차. 조건문

> 단계: 기초 | 선수: 3주차 (비교/논리 연산자, 입출력)

## 학습 목표
- `if`, `elif`, `else` 의 흐름을 이해한다
- 들여쓰기(indentation) 규칙을 지킨다
- 중첩 조건문을 사용한다
- 진리값(Truthy / Falsy)의 개념을 안다

## 1. if 문

조건이 True일 때만 들여쓰기 된 블록이 실행됩니다.

```python
score = 85
if score >= 60:
    print("합격!")
```

**들여쓰기는 4칸 공백** 이 표준. VS Code는 Tab을 4칸으로 자동 변환.

## 2. if-else

```python
score = 50
if score >= 60:
    print("합격")
else:
    print("불합격")
```

## 3. if-elif-else

여러 조건을 순서대로 검사. 처음으로 True인 분기만 실행되고 나머지는 건너뜀.

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

## 4. 중첩 조건문

조건문 안에 조건문. 너무 깊어지면 가독성 떨어지므로 2~3단계까지만.

```python
age = 17
if age >= 18:
    if age >= 65:
        print("경로 우대")
    else:
        print("성인")
else:
    print("미성년자")
```

## 5. 조건 표현식 (삼항 연산자)

한 줄로 분기를 처리. 간단한 경우에만 사용.

```python
n = 7
result = "짝수" if n % 2 == 0 else "홀수"
print(result)   # 홀수
```

## 6. 진리값(Truthy / Falsy)

`if 조건:` 에서 0, "", [], None, False 는 모두 거짓 처리됩니다.

```python
if "":
    print("실행 안 됨")
if 0:
    print("실행 안 됨")
if "hello":
    print("실행됨")
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_if_else.py` | 기본 if/else |
| `02_grade.py` | if/elif/else 학점 판정 |
| `03_nested.py` | 중첩 조건문 |
| `04_truthy.py` | Truthy/Falsy 동작 |

## ⚠️ 자주 하는 실수

1. **들여쓰기를 빠뜨리거나 섞음**
   ```python
   if x > 0:
   print("양수")   # IndentationError
   ```
   → 반드시 들여쓰기. 탭과 공백을 섞어 쓰면 보이지 않는 오류.

2. **`==` 대신 `=`**
   ```python
   if x = 5:        # SyntaxError
   if x == 5:       # 정상
   ```

3. **`elif` 대신 `else if`**
   파이썬은 `elif` 만 지원합니다. (Java/C 의 `else if` 와 다름)

4. **모든 분기에 `if` 만 사용**
   ```python
   if score >= 90:  # A
       print("A")
   if score >= 80:  # 80~89면 A, B 둘 다 출력됨!
       print("B")
   ```
   → 배타적 분기는 `elif` 사용.

5. **조건에 괄호를 강제**
   ```python
   if (x > 0):    # 동작은 하지만 권장 X
   if x > 0:      # 파이썬 스타일
   ```

## ❓ FAQ

**Q1. 조건이 여러 개 묶이는 경우는?**
A. `and`, `or` 사용. `if 0 < x < 100:` 같은 연쇄 비교도 가능 (파이썬 특유).

**Q2. `elif` 가 몇 개까지 가능한가요?**
A. 제한 없음. 다만 5개 이상 길어지면 딕셔너리 매핑 등 다른 구조를 고려.

**Q3. switch-case 문은 없나요?**
A. Python 3.10+ 부터 `match-case` 가 추가됐습니다. 입문 단계에서는 `if/elif` 로 충분.

## 📝 과제 (exercises/)

- `exercise1.md` — 학점 계산기
- `exercise2.md` — 윤년 판별기
- `exercise3.md` — 가위바위보 (1회)

## 다음 주차

[5주차. 반복문](../week05_반복문/) — 같은 동작을 여러 번 자동으로
