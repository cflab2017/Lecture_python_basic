# 7주차. 딕셔너리와 집합

> 단계: 기초 | 선수: 6주차 (리스트, 튜플)

## 학습 목표
- 딕셔너리 생성·키 접근·수정
- 자주 쓰는 메서드 (`get`, `items`, `keys`)
- 집합(set) 연산 (합집합/교집합/차집합)
- 자료구조 선택 기준

## 1. 딕셔너리란

**키(key) → 값(value)** 의 매핑. 순서 X (3.7+ 부터는 입력 순서 유지). 중괄호 `{...}`.

```python
student = {"name": "홍길동", "age": 20, "major": "CS"}

print(student["name"])      # 홍길동
student["age"] = 21         # 수정
student["email"] = "..."    # 추가
del student["major"]        # 삭제
```

키는 보통 **문자열** 또는 **숫자**, 값은 어떤 타입이든 가능.

## 2. 자주 쓰는 메서드

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())     # dict_keys(['a', 'b', 'c'])
print(d.values())   # dict_values([1, 2, 3])
print(d.items())    # dict_items([('a', 1), ...])

# get: 안전하게 조회 (키 없어도 에러 X)
print(d.get("z"))            # None
print(d.get("z", "기본값"))  # 기본값

# in: 키 존재 확인
print("a" in d)     # True
```

## 3. 딕셔너리 순회

```python
for key in d:                    # 키만
    print(key)

for key, value in d.items():     # 키-값 동시
    print(f"{key} = {value}")
```

## 4. 집합 (set)

**중복 없는** 원소의 모음. 순서 X. 중괄호 `{...}` (단, 빈 set은 `set()`).

```python
fruits = {"사과", "바나나", "포도"}
fruits.add("딸기")
fruits.discard("바나나")    # 없으면 무시
print(len(fruits))

# 중복 자동 제거
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)         # {1, 2, 3}
```

## 5. 집합 연산

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # 합집합 {1,2,3,4,5,6}
print(a & b)    # 교집합 {3,4}
print(a - b)    # 차집합 {1,2}
print(a ^ b)    # 대칭차 {1,2,5,6}
```

## 6. 자료구조 선택 기준

| 상황 | 선택 |
|------|------|
| 순서 중요, 인덱스로 접근 | 리스트 |
| 변경 불필요, 빠르게 | 튜플 |
| 키로 값 조회 | 딕셔너리 |
| 중복 제거, 멤버십 검사 | 집합 |

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_dict_basic.py` | 딕셔너리 생성/수정 |
| `02_dict_methods.py` | get, items, in 사용 |
| `03_set.py` | 집합 생성과 연산 |
| `04_word_count.py` | 단어 빈도 카운트 |

## ⚠️ 자주 하는 실수

1. **존재하지 않는 키 접근**
   ```python
   d = {"a": 1}
   print(d["z"])    # KeyError
   ```
   → `d.get("z")` 사용 또는 `if "z" in d:`.

2. **빈 set을 `{}`로 만들기**
   ```python
   s = {}    # 빈 딕셔너리!
   s = set() # 빈 set
   ```

3. **set에 리스트 넣기**
   ```python
   {[1, 2]}    # TypeError: unhashable type: 'list'
   {(1, 2)}    # 튜플은 OK
   ```

4. **딕셔너리 순회 중 수정**
   ```python
   for k in d:
       del d[k]   # RuntimeError
   ```
   → 키 목록을 미리 복사: `for k in list(d):`.

## ❓ FAQ

**Q1. 딕셔너리의 키 중복 시?**
A. 마지막 값으로 덮어씀. 키는 유일해야 함.

**Q2. 딕셔너리는 정렬되나요?**
A. Python 3.7+ 부터 **입력 순서 유지**. 정렬은 `sorted(d.items())`.

**Q3. 집합과 딕셔너리 둘 다 `{}` 인데 어떻게 구분?**
A. `:` 가 있으면 딕셔너리, 없으면 집합. `{1, 2}` = set, `{1: "a"}` = dict.

## 📝 과제 (exercises/)

- `exercise1.md` — 연락처 (딕셔너리)
- `exercise2.md` — 단어 빈도 Top 3
- `exercise3.md` — 중복 제거 (순서 유지)

## 다음 주차

[8주차. 문자열 다루기](../week08_문자열_다루기/) — 문자열 메서드 마스터
