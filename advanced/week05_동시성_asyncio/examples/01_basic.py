import asyncio

async def hello():
    print("hello")
    await asyncio.sleep(1)
    print("world")

async def main():
    await hello()
    print("done")

asyncio.run(main())
