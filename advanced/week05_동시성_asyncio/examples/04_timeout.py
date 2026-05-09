import asyncio

async def slow_task():
    await asyncio.sleep(3)
    return "결과"

async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=1.0)
        print(result)
    except asyncio.TimeoutError:
        print("시간 초과 (1초)")

asyncio.run(main())
