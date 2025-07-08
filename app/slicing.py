import time

def countdown(n):
    while n > 0:
        yield n
        n -= 1
        time.sleep(1)

for i in countdown(40):
    print(i)