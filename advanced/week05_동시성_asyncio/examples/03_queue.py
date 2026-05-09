import asyncio

async def producer(q, n):
    for i in range(n):
        await q.put(i)
        print(f"  생산: {i}")
        await asyncio.sleep(0.1)
    await q.put(None)

async def consumer(q):
    while True:
        item = await q.get()
        if item is None:
            break
        print(f"소비: {item}")
        await asyncio.sleep(0.05)

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q, 5), consumer(q))

asyncio.run(main())
