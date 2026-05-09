import time
from functools import wraps

def cached(func):
    cache = {}
    hits = misses = 0

    @wraps(func)
    def wrapper(*args):
        nonlocal hits, misses
        if args in cache:
            hits += 1
            return cache[args]
        misses += 1
        cache[args] = func(*args)
        return cache[args]

    def info():
        return {"hits": hits, "misses": misses, "size": len(cache)}

    wrapper.cache_info = info
    return wrapper

@cached
def slow_square(n):
    time.sleep(0.1)
    return n * n

start = time.perf_counter()
slow_square(5)
slow_square(5)
slow_square(5)
slow_square(7)
elapsed = time.perf_counter() - start
print(f"총 시간: {elapsed:.3f}s (캐시 없으면 ~0.4s)")
print(slow_square.cache_info())
