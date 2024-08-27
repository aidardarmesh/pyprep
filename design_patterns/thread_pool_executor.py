"""
Used for better resource utilization when processing large amount of tasks:
* Batch Processing
* Load Balancing
"""

from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Executing task {n}")
    time.sleep(1)
    print(f"Completed task {n}")

with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(10):
        executor.submit(task, i)

