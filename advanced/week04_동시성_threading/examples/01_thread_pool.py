import time
from concurrent.futures import ThreadPoolExecutor

def slow_io(n):
    time.sleep(0.5)   # 네트워크/파일 대기 시뮬레이션
    return n * 10

# 순차
start = time.perf_counter()
results = [slow_io(i) for i in range(8)]
print(f"순차: {time.perf_counter() - start:.2f}s, {results}")

# 스레드 풀
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(slow_io, range(8)))
print(f"스레드: {time.perf_counter() - start:.2f}s, {results}")
