import asyncio

async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)
    print('Done fetching')
    return {'data': 1}

async def main():
    print('Before fetching')
    result = await fetch_data()
    print('Result:', result)
    print('After fetching')

asyncio.run(main())
