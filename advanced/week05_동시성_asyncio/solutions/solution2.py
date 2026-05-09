import asyncio

async def producer(q, n):
    for i in range(n):
        await q.put(i)
    for _ in range(3):
        await q.put(None)   # 종료 신호 3개 (worker 수 만큼)

async def worker(name, q, results):
    while True:
        item = await q.get()
        if item is None:
            break
        results.append(item * item)

async def main():
    q = asyncio.Queue()
    results = []
    workers = [worker(f"w{i}", q, results) for i in range(3)]
    await asyncio.gather(producer(q, 100), *workers)
    print(f"결과 개수: {len(results)}, 합계: {sum(results)}")

asyncio.run(main())
