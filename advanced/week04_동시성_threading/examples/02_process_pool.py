import time
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    workload = [1_000_000] * 4

    start = time.perf_counter()
    serial = [heavy(n) for n in workload]
    print(f"순차: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        parallel = list(ex.map(heavy, workload))
    print(f"프로세스: {time.perf_counter() - start:.2f}s")

    print("결과 동일:", serial == parallel)
