import time
from concurrent.futures import ThreadPoolExecutor

# requests 없으면 동작하지 않음. 시뮬레이션:
def fetch(url):
    time.sleep(0.5)   # 네트워크 시뮬레이션
    return f"{url}: 1234 bytes"

URLS = [f"https://example.com/{i}" for i in range(8)]

start = time.perf_counter()
serial = [fetch(u) for u in URLS]
print(f"순차: {time.perf_counter() - start:.2f}s")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=8) as ex:
    parallel = list(ex.map(fetch, URLS))
print(f"스레드: {time.perf_counter() - start:.2f}s")
