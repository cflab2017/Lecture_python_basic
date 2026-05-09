import asyncio

async def task(name, delay):
    print(f"{name} 시작")
    await asyncio.sleep(delay)
    print(f"{name} 완료")
    return name

async def main():
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 1),
    )
    print("결과:", results)

import time
start = time.perf_counter()
asyncio.run(main())
print(f"총 {time.perf_counter() - start:.2f}s")
