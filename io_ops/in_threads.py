import requests
import time
import threading


def countdown():
    i = 0
    begin = time.time()
    while i < 5_000_000:
        i += 1
    print(f"duration:	{time.time() - begin}")


if __name__ == '__main__':
    begin = time.time()
    threads = []

    for i in range(10):
        thread_1 = threading.Thread(target=countdown)
        thread_1.start()
        threads.append(thread_1)

    for thread in threads:
        thread.join()

    print(time.time() - begin)

