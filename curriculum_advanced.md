# 파이썬 강의 - 고급 과정

> 본 과정은 **기초 / 중급 / 고급 / 실습과제** 4단계 커리큘럼 중 **3단계 (고급)** 입니다.
> 모든 주차는 **예제 중심**으로 진행하며, 매 주차마다 **과제**를 부여합니다.

## 강의 개요

- **대상**: 중급 과정을 이수한 학습자
- **기간**: 총 10주 (주 1회, 회당 2시간 / 총 20시간)
- **선수 지식**: 중급 과정 (OOP, 예외 처리, 파일 I/O, 모듈/패키지)
- **수업 방식**:
  - 이론 설명 30%, 라이브 코딩 예제 40%, 실습 30%
  - 매 주차 **3~4개의 핵심 예제** 직접 작성
  - 매 주차 **과제 2~3개** 제출
- **학습 목표**:
  - 타입 힌트와 정적 분석으로 견고한 코드를 작성한다
  - 데코레이터·컨텍스트 매니저를 직접 구현하고 활용한다
  - 동시성(threading, asyncio)으로 효율적인 프로그램을 만든다
  - 테스트 주도 개발(TDD)을 경험한다
  - 외부 라이브러리(requests, NumPy, Pandas)로 실무 작업을 수행한다
  - 자신의 패키지를 만들어 배포할 수 있다

---

## 주차별 커리큘럼

### 1주차. 타입 힌트와 dataclass

**학습 목표**: 정적 타입을 활용해 코드 안정성을 높인다

**핵심 예제**

```python
# 예제 1. 기본 타입 힌트
def greet(name: str, age: int = 20) -> str:
    return f"{name}({age})"

# 예제 2. typing 모듈
from typing import Optional
def find_user(uid: int) -> Optional[dict]:
    return None  # 사용자 없음

# 예제 3. dataclass
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    tags: list[str] = field(default_factory=list)

b = Book("Python", "Guido")
b.tags.append("language")
print(b)

# 예제 4. mypy로 정적 검사
# pip install mypy
# mypy main.py
```

**과제**
1. 기존 중급 종합 실습 코드에 타입 힌트 추가 후 `mypy --strict` 통과
2. `dataclass` 로 `Book`, `Member`, `Loan` 모델 작성
3. `Optional`, `list[T]`, `dict[str, T]` 를 사용한 함수 시그니처 5개

---

### 2주차. 데코레이터와 컨텍스트 매니저

**학습 목표**: 기능을 횡단 적용하고 자원을 안전하게 관리한다

**핵심 예제**

```python
# 예제 1. 함수 데코레이터
import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timed
def compute():
    return sum(i * i for i in range(1_000_000))

compute()

# 예제 2. 인자 받는 데코레이터
def retry(times: int):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"재시도 {i+1}/{times}: {e}")
            raise
        return wrapper
    return deco

# 예제 3. 클래스 기반 컨텍스트 매니저
class FileLock:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        print(f"잠금: {self.path}")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("해제")

with FileLock("data.txt"):
    print("작업 중")

# 예제 4. contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter() - start:.4f}s")

with timer("작업"):
    sum(range(1_000_000))
```

**과제**
1. 함수 호출을 로그 파일에 남기는 `@logged` 데코레이터
2. `@cached` 데코레이터로 결과 메모이제이션 (단순 dict)
3. `with timer("..."):` 처럼 사용할 수 있는 타이머 컨텍스트 매니저

---

### 3주차. 이터레이터·제너레이터 심화

**학습 목표**: 반복 프로토콜과 코루틴 기초를 이해한다

**핵심 예제**

```python
# 예제 1. 직접 이터레이터 구현
class Range:
    def __init__(self, start, stop):
        self.cur, self.stop = start, stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.cur >= self.stop:
            raise StopIteration
        self.cur += 1
        return self.cur - 1

print(list(Range(1, 5)))   # [1, 2, 3, 4]

# 예제 2. yield from
def chain(*iters):
    for it in iters:
        yield from it

print(list(chain([1, 2], (3, 4), "ab")))

# 예제 3. itertools 활용
import itertools
print(list(itertools.combinations([1, 2, 3, 4], 2)))
print(list(itertools.islice(itertools.count(1, 2), 5)))   # 1 3 5 7 9

# 예제 4. send로 코루틴 흉내
def echo():
    while True:
        x = yield
        print(f"받음: {x}")

co = echo()
next(co)
co.send("hello")
co.send("world")
```

**과제**
1. 큰 텍스트 파일을 N줄씩 묶어 yield 하는 `chunked_lines(path, n)` 제너레이터
2. `itertools.groupby` 로 정렬된 로그를 날짜별로 그룹화
3. 무한 피보나치 제너레이터 + `islice` 로 처음 20개만 추출

---

### 4주차. 동시성 (1) — 스레드와 프로세스

**학습 목표**: I/O·CPU 작업에 맞는 동시성 도구를 선택한다

**핵심 예제**

```python
# 예제 1. ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import requests

urls = ["https://example.com"] * 10

def fetch(url):
    return len(requests.get(url).text)

with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(fetch, urls))
print(results)

# 예제 2. ProcessPoolExecutor (CPU 작업)
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        print(list(ex.map(heavy, [1_000_000] * 4)))

# 예제 3. threading.Lock
import threading
counter = 0
lock = threading.Lock()

def inc():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

ts = [threading.Thread(target=inc) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print(counter)
```

**과제**
1. URL 리스트를 받아 동시에 다운로드하고 응답 크기를 출력 (스레드 풀)
2. CPU 바운드 작업(소수 판별 1~100만)을 프로세스 풀로 가속, 시간 비교
3. 공유 카운터에 Lock을 적용하기 전후 결과 차이 관찰

---

### 5주차. 동시성 (2) — asyncio

**학습 목표**: `async/await` 로 효율적인 I/O 동시성을 구현한다

**핵심 예제**

```python
# 예제 1. 코루틴 기본
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} 완료")

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 1),
    )

asyncio.run(main())

# 예제 2. 비동기 HTTP (httpx)
import httpx

async def fetch(client, url):
    r = await client.get(url)
    return len(r.text)

async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*[fetch(client, "https://example.com") for _ in range(10)])
    print(results)

asyncio.run(main())

# 예제 3. 큐를 이용한 producer/consumer
async def producer(q):
    for i in range(5):
        await q.put(i)
        await asyncio.sleep(0.1)
    await q.put(None)

async def consumer(q):
    while True:
        item = await q.get()
        if item is None: break
        print("처리:", item)
```

**과제**
1. `asyncio.gather` 로 10개 URL을 동시에 fetch, 총 소요시간 측정
2. 비동기 producer/consumer로 작업 큐 구현
3. `asyncio.wait_for` 로 타임아웃이 있는 fetch 작성

---

### 6주차. 테스트 (unittest, pytest)

**학습 목표**: 테스트로 코드 변경의 안전망을 확보한다

**핵심 예제**

```python
# 예제 1. pytest 기본
# test_calc.py
def add(a, b): return a + b

def test_add():
    assert add(2, 3) == 5

# pytest test_calc.py

# 예제 2. parametrize
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# 예제 3. fixture
@pytest.fixture
def sample_users():
    return [{"name": "Alice"}, {"name": "Bob"}]

def test_first(sample_users):
    assert sample_users[0]["name"] == "Alice"

# 예제 4. mock
from unittest.mock import patch

def get_weather(city):
    import requests
    return requests.get(f"https://api/{city}").json()

def test_get_weather():
    with patch("requests.get") as m:
        m.return_value.json.return_value = {"temp": 20}
        assert get_weather("seoul") == {"temp": 20}
```

**과제**
1. 중급 7~8주차 OOP 코드(`BankAccount`, `Stack`)에 pytest 테스트 작성
2. `parametrize` 로 다양한 입력 케이스 검증
3. 외부 API 호출 함수에 mock을 적용해 네트워크 없이 테스트

---

### 7주차. 외부 라이브러리 — 웹 스크래핑

**학습 목표**: requests + BeautifulSoup으로 웹 데이터를 수집한다

**핵심 예제**

```python
# 예제 1. requests
import requests
r = requests.get("https://news.ycombinator.com")
print(r.status_code, len(r.text))

# 예제 2. BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
for a in soup.select(".titleline > a")[:5]:
    print(a.get_text(), "->", a.get("href"))

# 예제 3. 헤더와 세션
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})
r = session.get("https://example.com")

# 예제 4. JSON API 호출
r = requests.get("https://api.github.com/users/python")
data = r.json()
print(data["public_repos"])
```

**과제**
1. 뉴스 사이트 헤드라인 Top 10 추출 후 CSV 저장
2. GitHub API로 특정 사용자의 저장소 목록과 별 개수 출력
3. robots.txt를 확인하고 허용된 경로만 크롤링하는 함수

---

### 8주차. 데이터 처리 입문 (NumPy, Pandas)

**학습 목표**: 표/배열 데이터를 NumPy·Pandas로 다룬다

**핵심 예제**

```python
# 예제 1. NumPy 기본
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a.mean(), a.std(), a * 2)

m = np.arange(12).reshape(3, 4)
print(m, m.shape, m.sum(axis=0))

# 예제 2. Pandas DataFrame
import pandas as pd
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [92, 78, 85],
    "dept": ["A", "B", "A"],
})
print(df.describe())
print(df[df.score >= 80])
print(df.groupby("dept")["score"].mean())

# 예제 3. CSV 읽기 + 전처리
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
print(monthly)

# 예제 4. 시각화 (matplotlib 연동)
monthly.plot(kind="bar")
```

**과제**
1. `students.csv` 를 읽어 학과별 평균/최고/최저 점수 구하기
2. NumPy로 1000명의 키·몸무게를 시뮬레이션하고 BMI 통계 출력
3. 매출 CSV에서 월별·카테고리별 합계 피벗 테이블 생성

---

### 9주차. 패키징과 배포

**학습 목표**: 자신의 패키지를 만들어 PyPI에 올린다

**핵심 예제**

```toml
# 예제 1. pyproject.toml
[project]
name = "mytool"
version = "0.1.0"
description = "My CLI tool"
requires-python = ">=3.10"
dependencies = ["requests"]

[project.scripts]
mytool = "mytool.cli:main"

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
```

```bash
# 예제 2. 빌드와 설치
pip install build
python -m build
pip install dist/mytool-0.1.0-py3-none-any.whl

# 예제 3. 가상환경
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

# 예제 4. PyPI 업로드 (TestPyPI)
pip install twine
twine upload --repository testpypi dist/*
```

**과제**
1. 중급 종합 실습 결과물을 `pyproject.toml` 기반 패키지로 변환
2. `console_scripts` 로 터미널에서 직접 실행되는 CLI 만들기
3. TestPyPI에 업로드해 다른 환경에서 `pip install` 로 설치 검증

---

### 10주차. 고급 종합 실습

**학습 목표**: 비동기·외부 라이브러리·테스트·배포를 통합한 실전 프로젝트

**핵심 예제 (비동기 크롤러 + 데이터 분석 골격)**

```python
import asyncio
import httpx
import pandas as pd
from dataclasses import dataclass

@dataclass
class Article:
    title: str
    score: int
    url: str

async def fetch_articles(client) -> list[Article]:
    r = await client.get("https://news.ycombinator.com")
    # ... BeautifulSoup 파싱
    return [...]

async def main():
    async with httpx.AsyncClient() as c:
        articles = await fetch_articles(c)
    df = pd.DataFrame([a.__dict__ for a in articles])
    df.to_csv("hn.csv", index=False)
    print(df.describe())

asyncio.run(main())
```

**과제 (택 1, 최종 제출)**
1. **비동기 크롤러 + 분석**: 뉴스/쇼핑 사이트 데이터를 비동기 수집 → Pandas 분석 → CSV 리포트
2. **CLI 도구 패키지**: argparse + 외부 API 호출 + 테스트 + PyPI 배포
3. **데이터 파이프라인**: CSV/JSON → 정제 → 집계 → 시각화 (matplotlib)
4. **자동화 봇**: 슬랙/디스코드 웹훅 + 스케줄러로 일일 리포트 전송

**제출물**
- 패키지 구조(`pyproject.toml`, 모듈 분리)
- 타입 힌트 + `mypy` 통과
- pytest 테스트 (커버리지 70% 이상 권장)
- README (설치법, 사용법, 예시)

---

## 평가 방식

| 항목 | 비중 |
|------|------|
| 출석 | 10% |
| 주차별 과제 (1~9주차) | 35% |
| 중간 발표 (5주차) | 15% |
| 최종 프로젝트 (10주차) | 40% |

**과제 채점 기준**
- 정확성 / 동작 — 30%
- 코드 품질 (타입 힌트, 모듈 분리) — 25%
- 테스트 — 20%
- 문서화·배포 — 15%
- 응용·도전 — 10%

---

## 다음 단계

고급 과정을 마치면 본격적인 **실습과제(curriculum_practice.md)** 의 Lv ★★★★ 도전이 가능합니다.

- 9주차 패키징 → 실습 13번 argparse CLI 도구
- 7주차 웹 스크래핑 → 실습 14번 CSV 분석 CLI
- 5주차 asyncio → 실습 15번 콘솔 챗봇 (API 모드)

이후 권장 학습 방향:
- **백엔드**: FastAPI / Django
- **데이터·ML**: PyTorch / scikit-learn
- **자동화·DevOps**: Ansible / Airflow

---

## 추천 학습 자료

- [Effective Python (Brett Slatkin)](https://effectivepython.com/)
- [Real Python — Advanced](https://realpython.com/tutorials/advanced/)
- [Python 공식 문서 — typing, asyncio](https://docs.python.org/ko/3/library/)
- [Awesome Python](https://github.com/vinta/awesome-python)
- 연습: [LeetCode Medium](https://leetcode.com), [Advent of Code](https://adventofcode.com)
