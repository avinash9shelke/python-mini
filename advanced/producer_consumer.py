from queue import Queue
from threading import Thread
import time

shared_queue = Queue()

def producer_items():
    for i in range(10):
        shared_queue.put(i)
        print(f'Producer added {i} to queue')
        time.sleep(0.1)

def consumer_items():
    for i in range(10):
        item = shared_queue.get()
        print(f'Consumer got {item} from queue')
        time.sleep(0.2)

# Create threads
producer_thread = Thread(target=producer_items)
consumer_thread = Thread(target=consumer_items)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()

print("Processing complete.")



