# 5주차. 반복문

> 단계: 기초 | 선수: 4주차 (조건문)

## 학습 목표
- `for` 와 `range()` 로 정해진 횟수만큼 반복한다
- `while` 로 조건이 참인 동안 반복한다
- `break`, `continue` 로 흐름을 제어한다
- 중첩 반복문을 이해한다

## 1. for 반복문

`range(시작, 끝, 간격)` 으로 정수 시퀀스를 만들어 반복.

```python
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11):       # 1 ~ 10
    print(i, end=" ")

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
    print(i)
```

리스트나 문자열 같은 시퀀스를 직접 순회할 수도 있습니다 (다음 주차).

## 2. while 반복문

조건이 True 인 동안 계속 실행. 반드시 **종료 조건**이 변해야 합니다.

```python
n = 1
while n <= 5:
    print(n)
    n += 1   # 이게 없으면 무한 루프!
```

사용자 입력으로 종료 결정:
```python
while True:
    cmd = input("명령(quit으로 종료): ")
    if cmd == "quit":
        break
    print(f"실행: {cmd}")
```

## 3. break 와 continue

- `break` — 반복문 즉시 탈출
- `continue` — 이번 반복 건너뛰고 다음으로

```python
for i in range(1, 11):
    if i == 5:
        continue   # 5는 건너뛰기
    if i == 8:
        break      # 8에서 종료
    print(i, end=" ")   # 1 2 3 4 6 7
```

## 4. 중첩 반복문

반복문 안의 반복문. 구구단·표 출력에 자주 사용.

```python
for i in range(2, 10):           # 2단~9단
    for j in range(1, 10):       # ×1 ~ ×9
        print(f"{i} × {j} = {i*j}")
    print()                      # 단 사이 공백
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_for_range.py` | for + range 패턴 |
| `02_while.py` | while 반복문 |
| `03_break_continue.py` | break, continue |
| `04_nested.py` | 중첩 반복문 (구구단) |

## ⚠️ 자주 하는 실수

1. **무한 루프**
   ```python
   n = 1
   while n <= 5:
       print(n)
       # n += 1 빠뜨림 → 무한히 1 출력
   ```
   → Ctrl+C 로 강제 종료. 종료 조건이 변하는지 확인.

2. **`range(1, 10)` 이 1~10이라고 착각**
   `range(1, 10)` 은 1~9 (10 미포함). 1~10 원하면 `range(1, 11)`.

3. **들여쓰기 누락**
   ```python
   for i in range(5):
   print(i)   # IndentationError
   ```

4. **`break` 가 모든 반복문을 빠져나간다고 오해**
   `break` 는 가장 가까운 반복문 하나만 빠져나갑니다. 다중 break은 플래그 변수 사용.

5. **반복 변수를 안에서 변경**
   ```python
   for i in range(5):
       i = 100   # 다음 반복에서 다시 0,1,2... 됨
   ```

## ❓ FAQ

**Q1. for와 while 중 언제 뭘 쓰나요?**
A. **횟수가 정해져 있으면 for**, **조건에 따라 끝나면 while**. 사용자 입력 받기는 보통 while.

**Q2. `for ... else` 문이 있다는데?**
A. `for` 가 정상 종료(break 없이)되면 `else` 가 실행됩니다. 입문 단계에서는 잘 안 씀.

**Q3. 0부터 시작하는 이유는?**
A. 컴퓨터가 인덱스를 0부터 세는 관행입니다. 사람에게 보여줄 땐 `enumerate(seq, start=1)` 로 1부터 시작 가능.

## 📝 과제 (exercises/)

- `exercise1.md` — 구구단 (2~9단)
- `exercise2.md` — 별 찍기 (정삼각형 + 역삼각형)
- `exercise3.md` — 숫자 맞추기 게임

## 다음 주차

[6주차. 리스트와 튜플](../week06_리스트와_튜플/) — 여러 개의 값을 한꺼번에
