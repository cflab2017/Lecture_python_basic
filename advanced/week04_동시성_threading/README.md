# 4주차. 동시성 (1) — 스레딩과 멀티프로세싱

> 단계: 고급 | 선수: 3주차

## 학습 목표
- I/O 바운드 vs CPU 바운드 작업 구분
- `ThreadPoolExecutor` 로 I/O 작업 가속
- `ProcessPoolExecutor` 로 CPU 작업 가속
- GIL의 의미를 이해한다
- `threading.Lock` 으로 동기화

## 1. GIL (Global Interpreter Lock)

CPython은 한 번에 하나의 스레드만 파이썬 바이트코드를 실행 → CPU 바운드 작업은 스레딩으로 가속 X. **I/O 작업 (네트워크, 디스크) 에서는 효과 있음**.

| 작업 종류 | 도구 |
|----------|------|
| I/O 바운드 (네트워크, 파일) | threading, asyncio |
| CPU 바운드 (계산, 인코딩) | multiprocessing |

## 2. ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor
import requests

urls = ["https://example.com"] * 10

def fetch(url):
    return len(requests.get(url).text)

with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(fetch, urls))
```

순차 실행 대비 5배 정도 빨라짐 (네트워크 대기 시간 동안 다른 작업).

## 3. ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":   # Windows는 필수
    with ProcessPoolExecutor() as ex:
        print(list(ex.map(heavy, [1_000_000] * 4)))
```

## 4. submit / as_completed

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor() as ex:
    futures = [ex.submit(fetch, url) for url in urls]
    for fut in as_completed(futures):
        print(fut.result())
```

## 5. threading.Lock

여러 스레드가 같은 자원을 변경할 때 데이터 깨짐 방지.

```python
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
print(counter)   # 400000
```

Lock 없으면 결과가 작거나 가변적임.

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_thread_pool.py` | ThreadPoolExecutor (I/O) |
| `02_process_pool.py` | ProcessPoolExecutor (CPU) |
| `03_lock.py` | threading.Lock |
| `04_compare.py` | 순차 vs 스레드 시간 비교 |

## ⚠️ 자주 하는 실수

1. **CPU 작업에 thread 사용** — GIL 때문에 느려질 수도
2. **`__main__` 가드 누락** (Windows + multiprocessing) — 무한 루프
3. **공유 자원에 Lock 누락** — 결과 비결정적
4. **Future 결과 안 받음** — 예외가 묻힘

## ❓ FAQ

**Q1. asyncio 와 비교하면?**
A. asyncio는 단일 스레드에서 협력적. threading은 OS가 스케줄링. I/O 가벼우면 asyncio, 라이브러리 호환성 중요하면 threading.

**Q2. multiprocessing 의 단점?**
A. 프로세스 시작 비용 큼. 작은 작업은 오히려 느림. 객체 직렬화(pickle) 필요.

## 📝 과제 (exercises/)

- `exercise1.md` — 다중 URL 동시 다운로드 (시간 비교)
- `exercise2.md` — CPU 작업 프로세스 풀 가속
- `exercise3.md` — 공유 카운터 + Lock 적용 전후 비교

## 다음 주차

[5주차. 동시성 (2) - asyncio](../week05_동시성_asyncio/)
