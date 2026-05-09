import asyncio
import random

async def task(i):
    delay = random.uniform(0.1, 3.0)
    await asyncio.sleep(delay)
    return f"task{i} ({delay:.2f}s)"

async def with_timeout(coro, timeout):
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return None

async def main():
    coros = [with_timeout(task(i), 1.5) for i in range(10)]
    results = await asyncio.gather(*coros)
    for i, r in enumerate(results):
        print(f"{i}: {r if r else '시간초과'}")

asyncio.run(main())
