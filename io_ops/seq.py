import requests
import time

begin = time.time()

for i in range(10):
    req = requests.get('https://api.covidtracking.com/v1/us/current.json')

print(time.time() - begin)