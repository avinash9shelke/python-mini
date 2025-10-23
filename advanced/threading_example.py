import time
from threading import Thread

value = 0


def increment():
    global value

    temp_value = value
    temp_value += 1
    time.sleep(0.1)
    value = temp_value


if __name__ == '__main__':
    thread1 = Thread(target=increment)
    thread2 = Thread(target=increment)
    print(f'Start Value: {value}')
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'End Value: {value}')
