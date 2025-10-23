import time
from threading import Thread,Lock

value = 0


def increment(thread_lock: Lock):
    global value

    thread_lock.acquire() # with lock: - auto lock acquire and release

    temp_value = value
    temp_value += 1
    time.sleep(0.1)
    value = temp_value

    thread_lock.release()


if __name__ == '__main__':

    lock = Lock()

    thread1 = Thread(target=increment,args=(lock,))
    thread2 = Thread(target=increment,args=(lock,))
    print(f'Start Value: {value}')
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'End Value: {value}')
