from multiprocessing import Process
import requests
import time


def countdown():
    i = 0
    begin = time.time()
    while i < 5_000_000:
        i += 1
    print(f"duration:	{time.time() - begin}")


if __name__ == '__main__':
    begin = time.time()
    procs = []

    for i in range(10):
        proc = Process(target=countdown)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print(time.time() - begin)
