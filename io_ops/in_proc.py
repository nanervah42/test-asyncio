from multiprocessing import Process
import requests
import time


def t1(int):
    req = requests.get('https://api.covidtracking.com/v1/us/current.json')
    print(req)


if __name__ == '__main__':
    begin = time.time()
    procs = []

    for i in range(10):
        proc = Process(target=t1, args=(1,))
        procs.append(proc)
        proc.start()


    for proc in procs:
        proc.join()

    print(time.time() - begin)