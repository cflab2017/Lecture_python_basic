from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield               # with 블록 실행
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")

with timer("합계"):
    total = sum(range(1_000_000))

with timer("정렬"):
    sorted(range(100_000), reverse=True)
