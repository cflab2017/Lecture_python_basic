import asyncio
import time

async def fetch(url):
    await asyncio.sleep(0.5)
    return f"{url}: 1024 bytes"

URLS = [f"https://example.com/{i}" for i in range(10)]

async def serial():
    return [await fetch(u) for u in URLS]

async def parallel():
    return await asyncio.gather(*[fetch(u) for u in URLS])

start = time.perf_counter()
asyncio.run(serial())
print(f"순차: {time.perf_counter() - start:.2f}s")

start = time.perf_counter()
asyncio.run(parallel())
print(f"동시: {time.perf_counter() - start:.2f}s")
