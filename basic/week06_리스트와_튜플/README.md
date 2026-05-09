# 6주차. 리스트와 튜플

> 단계: 기초 | 선수: 5주차 (반복문)

## 학습 목표
- 리스트 생성·인덱싱·슬라이싱
- 자주 쓰는 리스트 메서드 (`append`, `pop`, `sort` 등)
- 튜플의 특징과 언패킹
- 리스트 vs 튜플의 차이

## 1. 리스트

여러 값을 순서대로 담는 자료구조. 대괄호 `[...]`.

```python
fruits = ["사과", "바나나", "포도"]
print(fruits[0])    # 사과
print(fruits[-1])   # 포도 (음수 = 뒤에서)
print(len(fruits))  # 3
```

## 2. 슬라이싱

`[시작:끝:간격]`. 끝은 포함하지 않음.

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]
print(nums[2:])      # [30, 40, 50]
print(nums[::-1])    # [50, 40, 30, 20, 10] (역순)
print(nums[::2])     # [10, 30, 50]
```

## 3. 자주 쓰는 메서드

| 메서드 | 동작 |
|--------|------|
| `append(x)` | 끝에 추가 |
| `insert(i, x)` | i 위치에 삽입 |
| `pop()` / `pop(i)` | 마지막 / i번째 제거하고 반환 |
| `remove(x)` | x 값 제거 |
| `sort()` | 정렬 (제자리) |
| `reverse()` | 뒤집기 (제자리) |
| `index(x)` | x의 위치 |
| `count(x)` | x의 개수 |

```python
nums = [3, 1, 4, 1, 5]
nums.append(9)        # [3, 1, 4, 1, 5, 9]
nums.sort()           # [1, 1, 3, 4, 5, 9]
nums.reverse()        # [9, 5, 4, 3, 1, 1]
print(nums.count(1))  # 2
```

## 4. 순회와 enumerate

```python
fruits = ["사과", "바나나", "포도"]

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}번: {fruit}")
```

## 5. 튜플

리스트와 비슷하지만 **변경 불가능** (immutable). 소괄호 `(...)`.

```python
point = (10, 20)
x, y = point          # 언패킹
print(x, y)           # 10 20

# 튜플은 수정 불가
# point[0] = 5         # TypeError
```

## 6. 리스트 vs 튜플

| | 리스트 | 튜플 |
|---|--------|------|
| 문법 | `[...]` | `(...)` |
| 변경 | 가능 | 불가 |
| 용도 | 자주 바뀌는 데이터 | 고정 데이터 (좌표, RGB 등) |
| 속도 | 느림 | 빠름 |

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_list_basic.py` | 리스트 생성·인덱싱 |
| `02_slicing.py` | 슬라이싱 |
| `03_methods.py` | append/pop/sort 등 |
| `04_tuple.py` | 튜플과 언패킹 |

## ⚠️ 자주 하는 실수

1. **인덱스 범위 초과**
   ```python
   a = [1, 2, 3]
   print(a[3])   # IndexError
   ```
   → 마지막은 `a[-1]` 또는 `a[len(a)-1]`.

2. **`sort()` 의 반환값을 변수에 할당**
   ```python
   sorted_list = nums.sort()   # None! 제자리 정렬이라 반환값 없음
   ```
   → `nums.sort()` 후 `nums` 자체가 정렬됨. 새 리스트 원하면 `sorted(nums)`.

3. **리스트 복사 함정**
   ```python
   a = [1, 2, 3]
   b = a          # 같은 리스트를 가리킴!
   b.append(4)
   print(a)       # [1, 2, 3, 4] — a도 바뀜
   ```
   → 복사하려면 `b = a.copy()` 또는 `b = a[:]`.

4. **빈 튜플 만들기**
   `()` 는 빈 튜플. 하나짜리 튜플은 `(5,)` (콤마 필수). `(5)` 는 그냥 정수 5.

## ❓ FAQ

**Q1. 리스트에 다른 타입을 섞어도 되나요?**
A. 네. `[1, "hi", True, [1,2]]` 가능. 다만 같은 타입을 권장.

**Q2. 슬라이스의 끝이 왜 미포함인가요?**
A. `range`, 인덱스 등과 일관성을 위해. 길이 계산이 `끝 - 시작` 으로 자연스러움.

**Q3. `sort()` 와 `sorted()` 의 차이는?**
A. `sort()` 는 메서드, 원본 변경. `sorted()` 는 함수, 새 리스트 반환.

## 📝 과제 (exercises/)

- `exercise1.md` — 학생 점수 통계
- `exercise2.md` — 로또 번호 생성기
- `exercise3.md` — 리스트 뒤집기 (두 가지 방법)

## 다음 주차

[7주차. 딕셔너리와 집합](../week07_딕셔너리와_집합/) — 키-값 매핑
