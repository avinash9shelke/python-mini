from threading import Thread
import os

def square_numbers():
    for n in range(10):
        print(f'Process {os.getpid()} square {n}')
        print(f'{n} * {n} = {n*n}')

threads = []
num_threads = os.cpu_count()

#Create threads
for i in range(num_threads):
    p = Thread(target=square_numbers)
    threads.append(p)

# Start threads
for p in threads:
    p.start()

# Join threads
for p in threads:
    p.join()

print('Done!')