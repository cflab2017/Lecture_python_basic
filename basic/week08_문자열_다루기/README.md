# 8주차. 문자열 다루기

> 단계: 기초 | 선수: 7주차 (자료구조)

## 학습 목표
- 문자열 인덱싱·슬라이싱
- 자주 쓰는 문자열 메서드 (`split`, `join`, `strip`, `replace` 등)
- f-string 심화 (정렬·자릿수)
- 이스케이프 문자 (`\n`, `\t`)

## 1. 문자열 기초

문자열은 **변경 불가능(immutable)**. 인덱싱과 슬라이싱은 리스트와 동일.

```python
s = "Python"
print(s[0])         # P
print(s[-1])        # n
print(s[1:4])       # yth
print(len(s))       # 6

# s[0] = "X"  # TypeError — 변경 불가
```

## 2. 자주 쓰는 메서드

| 메서드 | 동작 | 예시 |
|--------|------|------|
| `lower()` / `upper()` | 소/대문자 | `"Hi".upper()` → `"HI"` |
| `strip()` | 양쪽 공백 제거 | `" hi ".strip()` → `"hi"` |
| `lstrip()` / `rstrip()` | 좌/우 공백 제거 |
| `split(sep)` | 분리해서 리스트로 | `"a,b,c".split(",")` → `["a","b","c"]` |
| `join(seq)` | 리스트를 합치기 | `",".join(["a","b"])` → `"a,b"` |
| `replace(old, new)` | 치환 | `"foo".replace("o", "*")` → `"f**"` |
| `find(x)` / `index(x)` | 위치 찾기 | `"hello".find("l")` → `2` |
| `count(x)` | 개수 | `"hello".count("l")` → `2` |
| `startswith(x)` / `endswith(x)` | 시작/끝 검사 | `"abc".endswith("c")` → `True` |
| `isdigit()` / `isalpha()` | 숫자/문자 검사 |

## 3. f-string 심화

```python
name = "Alice"
score = 92.345

print(f"{name:<10}|")       # 좌측 정렬 폭 10
print(f"{name:>10}|")       # 우측 정렬
print(f"{name:^10}|")       # 가운데
print(f"{name:*^10}|")      # 채움 문자 * 가운데

print(f"{score:.2f}")        # 92.35  (소수점 둘째)
print(f"{1234567:,}")        # 1,234,567  (천 단위 콤마)
print(f"{0.85:.0%}")         # 85%
print(f"{255:b} {255:x}")    # 2진수, 16진수
```

## 4. 이스케이프 문자

| 표기 | 의미 |
|------|------|
| `\n` | 줄바꿈 |
| `\t` | 탭 |
| `\\` | 백슬래시 |
| `\"` | 큰따옴표 |
| `\'` | 작은따옴표 |

```python
print("줄1\n줄2")        # 두 줄
print("이름\t나이")      # 탭으로 구분
print("경로: C:\\dev")    # C:\dev

# raw string: 이스케이프 무시
print(r"C:\dev\new")      # C:\dev\new
```

## 5. 문자열과 리스트 변환

```python
csv = "사과,바나나,포도"
fruits = csv.split(",")             # ['사과', '바나나', '포도']

joined = " | ".join(fruits)         # "사과 | 바나나 | 포도"
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_methods.py` | 자주 쓰는 메서드 |
| `02_split_join.py` | split / join 패턴 |
| `03_fstring_format.py` | f-string 심화 |
| `04_escape.py` | 이스케이프 문자 |

## ⚠️ 자주 하는 실수

1. **문자열 원본을 수정하려 함**
   ```python
   s = "hello"
   s.replace("l", "L")    # s는 그대로!
   s = s.replace("l", "L")  # 결과를 다시 할당해야
   ```

2. **`split()` 인자 누락 시 분리 기준**
   `"a b c".split()` 은 공백 분리. `"a,b".split()` 은 분리 안 됨.

3. **`find` vs `index`**
   `find` 는 없으면 `-1`, `index` 는 `ValueError`.

4. **이스케이프 없이 따옴표 안에 같은 따옴표**
   ```python
   s = "say "hi""    # SyntaxError
   s = 'say "hi"'    # OK
   s = "say \"hi\""  # OK
   ```

5. **f-string 중괄호 출력**
   ```python
   print(f"{name}")     # 변수
   print(f"{{name}}")   # 그냥 {name} 출력
   ```

## ❓ FAQ

**Q1. 문자열 길이는 한글도 1글자로 세나요?**
A. `len()` 은 코드 포인트 단위라 보통 1글자. 이모지·결합문자는 예외 있음.

**Q2. 대소문자 무시하고 비교하려면?**
A. `s1.lower() == s2.lower()` 또는 `s1.casefold() == s2.casefold()` (더 정확).

**Q3. 문자열 안에 변수 값을 넣는 방법이 여럿?**
A. 옛 방식: `%` , `.format()`. 현재 권장: **f-string** (가장 빠르고 가독성 좋음).

## 📝 과제 (exercises/)

- `exercise1.md` — 회문(palindrome) 판별
- `exercise2.md` — 이메일 형식 검증
- `exercise3.md` — 텍스트 통계 (글자 수, 단어 수, 평균 길이)

## 다음 주차

[9주차. 함수 기초](../week09_함수_기초/) — 코드 재사용
