# 6주차. 파일 입출력 (텍스트·CSV·JSON)

> 단계: 중급 | 선수: 5주차 (예외 처리)

## 학습 목표
- 텍스트 파일을 `with open` 으로 안전하게 다룬다
- CSV 파일을 `csv` 모듈로 읽고 쓴다
- JSON으로 구조화된 데이터를 저장·로드한다

## 1. 텍스트 파일

### with 문 (권장)
파일을 자동으로 닫아줍니다.

```python
# 쓰기
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("첫 줄\n")
    f.writelines(["A\n", "B\n", "C\n"])

# 읽기
with open("notes.txt", encoding="utf-8") as f:
    content = f.read()      # 전체 한 번에
    # 또는
    for line in f:           # 한 줄씩
        print(line.rstrip())
```

### 모드
| 모드 | 의미 |
|------|------|
| `r` | 읽기 (기본) |
| `w` | 쓰기 (기존 내용 삭제) |
| `a` | 추가 |
| `r+` | 읽기/쓰기 |
| `b` | 바이너리 (예: `rb`, `wb`) |

⚠️ **항상 `encoding="utf-8"` 명시** (한글 안전).

## 2. CSV

쉼표로 구분된 표 형식.

```python
import csv

# 쓰기
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "score"])
    w.writerows([["Alice", 92], ["Bob", 78]])

# 읽기
with open("scores.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["score"])
```

⚠️ `newline=""` 빠뜨리면 빈 줄 생김 (Windows).

## 3. JSON

구조화된 데이터를 텍스트로 직렬화.

```python
import json

data = {
    "name": "홍길동",
    "skills": ["Python", "SQL"],
    "active": True,
}

# 저장
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 로드
with open("profile.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["skills"])
```

옵션:
- `ensure_ascii=False` — 한글을 그대로
- `indent=2` — 사람이 읽기 쉽게 들여쓰기

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_text.py` | 텍스트 파일 읽기/쓰기 |
| `02_csv_write.py` | CSV 쓰기 |
| `03_csv_read.py` | CSV 읽기 (DictReader) |
| `04_json.py` | JSON dump/load |

## ⚠️ 자주 하는 실수

1. **`open` 후 `close` 누락** — `with` 사용으로 자동 처리.
2. **`encoding` 누락** — Windows에서 한글 깨짐.
3. **`json.dump` vs `json.dumps`** — `dump` 는 파일에, `dumps` 는 문자열로.
4. **CSV `newline=""` 누락** — Windows에서 빈 줄 추가됨.
5. **JSON으로 저장 안 되는 타입** — `datetime`, 사용자 클래스. 변환 필요.

## ❓ FAQ

**Q1. CSV 와 JSON 중 뭘 쓰나요?**
A. **표 형태 데이터는 CSV**, **중첩·구조화 데이터는 JSON**.

**Q2. 큰 파일도 한 번에 읽어도 되나요?**
A. 메모리에 올라가므로 GB 단위는 위험. 라인 단위 순회 또는 제너레이터 사용.

**Q3. `pickle` 은 뭔가요?**
A. 파이썬 객체를 그대로 저장. 단, 다른 언어에서 못 읽고 보안 위험. JSON 권장.

## 📝 과제 (exercises/)

- `exercise1.md` — 메모장 (텍스트 추가)
- `exercise2.md` — CSV 점수 통계
- `exercise3.md` — To-Do JSON 영구 저장

## 다음 주차

[7주차. 객체지향 (1)](../week07_객체지향_1/)
