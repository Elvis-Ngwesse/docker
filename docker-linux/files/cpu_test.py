import multiprocessing
import time


def cpu_burn():
    while True:
        pass


for _ in range(multiprocessing.cpu_count()):
    multiprocessing.Process(target=cpu_burn).start()

time.sleep(5)
