"""
The workers could be threads within single application, 
separate processes on the same machine or different machines in a distributed system. 

Use cases:
* Data Transformation: distribute large dataset among multiple workers. 
* Task Parallelism: when tasks are independent of each other
* Distributed Computing

Components:
* Worker: performs a piece of task independently of others
* Queue: central component where tasks are stored awaiting processing
* Dispatcher (optionally): assigns tasks to workers based on availability, load and priority
"""

from multiprocessing import Process, Queue
import time

def worker(task_queue):
    while not task_queue.empty():
        task = task_queue.get()
        print(f"Worker {task} is processing")
        time.sleep(1)
        print(f"Worker {task} completed")

if __name__ == "__main__":
    task_queue = Queue()

    for i in range(10):
        task_queue.put(i)
    
    processes = [
        Process(target=worker, args=(task_queue,))
        for _ in range(5)
    ]

    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    
    print("All tasks completed.")
