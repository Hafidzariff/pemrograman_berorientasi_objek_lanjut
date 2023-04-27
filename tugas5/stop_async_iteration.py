import asyncio

async def countdown(num):
    while num > 0:
        print(num)
        await asyncio.sleep(1)
        num -= 1

    raise StopAsyncIteration

async def main():
    try:
        await countdown(5)
    except StopAsyncIteration:
        print("Countdown stopped!")

asyncio.run(main())