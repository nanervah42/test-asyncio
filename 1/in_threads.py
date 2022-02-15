import requests
import time
import threading


def t1():
    # req = requests.get('https://api.covidtracking.com/v1/us/current.json')
    req = requests.get('https://mail.ru')
    print(req)


if __name__ == '__main__':
    begin = time.time()
    threads = []

    for i in range(10):
        thread_1 = threading.Thread(target=t1)
        thread_1.start()
        threads.append(thread_1)

    for thread in threads:
        thread.join()

    print(time.time() - begin)

