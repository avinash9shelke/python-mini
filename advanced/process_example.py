from multiprocessing import Process
import os

def square_numbers():
    for n in range(10):
        print(f'Process {os.getpid()} square {n}')
        print(f'{n} * {n} = {n*n}')

processes = []
num_processes = os.cpu_count()

#Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# Start processes
for p in processes:
    p.start()

# Join processes
for p in processes:
    p.join()

print('Done!')