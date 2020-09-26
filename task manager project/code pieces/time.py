import time

while True:
    localtime = time.localtime()
    result = time.strftime("%H:%M:%S", localtime)
    print(result, end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)
