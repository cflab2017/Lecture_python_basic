import time
from concurrent.futures import ProcessPoolExecutor

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

def count_primes(start_end):
    start, end = start_end
    return sum(1 for n in range(start, end) if is_prime(n))

if __name__ == "__main__":
    LIMIT = 200_000

    start = time.perf_counter()
    total_serial = count_primes((2, LIMIT))
    print(f"순차: {time.perf_counter() - start:.2f}s, 소수 {total_serial}개")

    chunks = [(i, i + LIMIT // 4) for i in range(2, LIMIT, LIMIT // 4)]
    start = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        total_parallel = sum(ex.map(count_primes, chunks))
    print(f"프로세스: {time.perf_counter() - start:.2f}s, 소수 {total_parallel}개")
