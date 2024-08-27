"""
Future is value yet unknown but will be eventually (placeholder). 
Async operation until result is available unblocks itself by sharing Future. 
Promise is counterpart that eventually provides a value. 

Use cases:
* Data Pipelines: data is transformed by multiple stages. Representing each stage by Future doesn't block flow. 
* Task scheduling. 
* Complex database queries or transactions. 
* File I/O operations: by using Future and Promise file I/O operations can be offloaded to background. 

Steps:
* Initiation: involves async function that instead of waiting completion returns Future. 
Internally async function creates Promise. It's linked to Future. 
* Execution: proceeds independently of main flow. 
Once it's complete result is communicated back to part of program that initiated operation. 
The outcome is directly passed to previously created Promise. 
* Resolution: Promised is fulfilled or rejected. Using result is often done with callback or continuation function.
"""

# using concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    futures = []

    for i in range(3, 6):
        futures.append(executor.submit(square, i))
    
    for f in as_completed(futures):
        print(f"Result: {f.result()}")


# using asyncio
import asyncio

async def async_square(x):
    await asyncio.sleep(1)
    return x * x

async def main():
    async_futures = []

    for i in range(6, 9):
        async_futures.append(asyncio.ensure_future(async_square(i)))

    results = await asyncio.gather(*async_futures)

    for res in results:
        print(f"Result: {res}")

if __name__ == "__main__":
    asyncio.run(main())