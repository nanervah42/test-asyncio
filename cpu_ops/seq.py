import time

def countdown():
    i = 0
    begin = time.time()
    while i < 5_000_000:
        i += 1
    print(f"duration:	{time.time() - begin}")

for i in range(10):
    countdown()