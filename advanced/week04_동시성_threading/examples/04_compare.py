import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def io_task(n):
    time.sleep(0.2)
    return n

def cpu_task(n):
    return sum(i * i for i in range(n))

N = 8

print("=== I/O 바운드 ===")
for label, ex_class in [("순차", None), ("Thread", ThreadPoolExecutor), ("Process", ProcessPoolExecutor)]:
    start = time.perf_counter()
    if ex_class is None:
        [io_task(i) for i in range(N)]
    else:
        with ex_class(max_workers=N) as ex:
            list(ex.map(io_task, range(N)))
    print(f"{label}: {time.perf_counter() - start:.2f}s")

print("\n=== CPU 바운드 ===")
workload = [500_000] * N
for label, ex_class in [("순차", None), ("Thread", ThreadPoolExecutor), ("Process", ProcessPoolExecutor)]:
    start = time.perf_counter()
    if ex_class is None:
        [cpu_task(n) for n in workload]
    elif __name__ == "__main__" or ex_class is ThreadPoolExecutor:
        with ex_class() as ex:
            list(ex.map(cpu_task, workload))
    print(f"{label}: {time.perf_counter() - start:.2f}s")
