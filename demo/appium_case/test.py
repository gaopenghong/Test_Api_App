import time

name = lambda: int(round(time.time() * 1000*1000))
print(name())
