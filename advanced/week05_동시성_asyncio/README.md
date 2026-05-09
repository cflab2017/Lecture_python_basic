# 5주차. 동시성 (2) — asyncio

> 단계: 고급 | 선수: 4주차

## 학습 목표
- `async/await` 문법을 사용한다
- `asyncio.run`, `asyncio.gather` 로 동시 실행한다
- 비동기 HTTP 호출 (`httpx`, `aiohttp`)
- producer/consumer 패턴

## 1. 코루틴

`async def` 로 정의된 함수는 코루틴. 호출해도 즉시 실행 안 되고 객체 반환.

```python
import asyncio

async def hello():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(hello())
```

## 2. asyncio.gather

여러 코루틴을 동시 실행.

```python
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
# 약 2초 소요 (순차면 4초)
```

## 3. 비동기 HTTP

```python
import asyncio
import httpx

async def fetch(client, url):
    r = await client.get(url)
    return len(r.text)

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, "https://example.com") for _ in range(10)]
        results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

`requests` 는 동기, `httpx` 와 `aiohttp` 가 비동기.

## 4. producer / consumer

```python
async def producer(q):
    for i in range(5):
        await q.put(i)
        print(f"생산: {i}")
        await asyncio.sleep(0.1)
    await q.put(None)   # 종료 신호

async def consumer(q):
    while True:
        item = await q.get()
        if item is None:
            break
        print(f"소비: {item}")

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))
```

## 5. 타임아웃

```python
try:
    result = await asyncio.wait_for(slow_task(), timeout=1.0)
except asyncio.TimeoutError:
    print("시간 초과")
```

## 6. 동기 vs 비동기

| | 스레딩 | asyncio |
|---|--------|---------|
| 단위 | OS 스레드 | 코루틴 |
| 컨텍스트 스위칭 | OS가 결정 | `await` 에서만 |
| 메모리 | 무거움 | 가벼움 |
| 라이브러리 | 대부분 호환 | async 지원 필요 |

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_basic.py` | async/await 기본 |
| `02_gather.py` | gather 동시 실행 |
| `03_queue.py` | Queue producer/consumer |
| `04_timeout.py` | wait_for 타임아웃 |

## ⚠️ 자주 하는 실수

1. **`async def` 결과를 `await` 안 함** — 코루틴 객체만 반환됨, 실행 안 됨.
2. **동기 함수 안에서 `await`** — `await` 는 `async def` 안에서만.
3. **블로킹 함수 호출** — `time.sleep` 대신 `await asyncio.sleep`.
4. **asyncio.run 중첩** — Jupyter 등에서는 이미 루프가 있음. `await main()` 사용.

## ❓ FAQ

**Q1. `requests` 를 asyncio 안에서 쓸 수 있나요?**
A. 동작은 함. 하지만 블로킹이라 동시성 효과 없음. `httpx` 사용.

**Q2. asyncio.gather vs asyncio.wait?**
A. `gather` 는 결과를 순서대로 받음, 실패 시 전파. `wait` 는 더 유연.

**Q3. async 함수 디버깅이 어려워요.**
A. `traceback` 이 다소 복잡. PyCharm/VS Code 디버거가 도움.

## 📝 과제 (exercises/)

- `exercise1.md` — 동시 fetch 시간 측정
- `exercise2.md` — Queue 기반 작업 분배
- `exercise3.md` — 타임아웃이 있는 fetch

## 다음 주차

[6주차. 테스트](../week06_테스트/)
