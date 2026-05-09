# 4주차. 표준 라이브러리

> 단계: 중급 | 선수: 3주차 (모듈/패키지)

## 학습 목표
- `datetime` 으로 날짜·시간을 다룬다
- `random` 으로 무작위 값·샘플링
- `pathlib` 으로 파일·폴더 경로
- `collections` 의 `Counter`, `defaultdict`

표준 라이브러리는 추가 설치 없이 바로 import 가능합니다.

## 1. datetime

```python
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M"))

today = date.today()
birthday = date(2000, 5, 9)
days_lived = (today - birthday).days

next_week = now + timedelta(days=7)
```

## 2. random

```python
import random

print(random.random())                  # 0.0 ~ 1.0
print(random.randint(1, 100))           # 1 ~ 100 정수
print(random.choice(["가위","바위","보"]))
print(random.sample(range(1, 46), 6))   # 로또
random.shuffle(my_list)                 # 제자리 섞기
```

## 3. pathlib

문자열보다 깔끔한 경로 다루기.

```python
from pathlib import Path

p = Path("data") / "report.txt"        # data/report.txt
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hello", encoding="utf-8")
print(p.read_text(encoding="utf-8"))

print(p.exists(), p.suffix, p.name, p.stem)

# 폴더 내 파일 목록
for f in Path(".").glob("*.py"):
    print(f.name, f.stat().st_size)
```

## 4. collections

```python
from collections import Counter, defaultdict, deque

# Counter — 빈도 계산 한 줄
text = "to be or not to be"
print(Counter(text.split()))    # {'to': 2, 'be': 2, ...}
print(Counter(text.split()).most_common(2))

# defaultdict — 키가 없으면 기본값
groups = defaultdict(list)
for name, age in [("A", 20), ("B", 25), ("C", 20)]:
    groups[age].append(name)
print(dict(groups))

# deque — 양방향 큐
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_datetime.py` | 날짜/시간 |
| `02_random.py` | 무작위 |
| `03_pathlib.py` | 경로 |
| `04_collections.py` | Counter, defaultdict |

## ⚠️ 자주 하는 실수

1. **`datetime` vs `date`** — `datetime` 은 시간까지, `date` 는 날짜만.
2. **`random.seed()` 모름** — 같은 결과 재현하려면 `random.seed(42)` 처럼 시드 설정.
3. **경로 문자열 더하기** — `"data" + "/" + "x"` 보다 `Path("data") / "x"` 가 안전.

## ❓ FAQ

**Q1. `time` 과 `datetime` 의 차이?**
A. `time` 은 저수준(타임스탬프), `datetime` 은 고수준(객체). 보통 datetime 이면 충분.

**Q2. `os.path` 와 `pathlib` 중 뭐?**
A. 신규 코드는 `pathlib` 권장. 더 OOP스럽고 가독성 좋음.

## 📝 과제 (exercises/)

- `exercise1.md` — D-Day 계산기
- `exercise2.md` — 폴더 내 .txt 파일 크기 출력
- `exercise3.md` — 단어 빈도 Top 5 (Counter)

## 다음 주차

[5주차. 예외 처리](../week05_예외_처리/)
