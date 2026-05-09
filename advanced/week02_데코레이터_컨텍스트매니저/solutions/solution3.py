from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[timer] {label}: {elapsed:.4f}s")

with timer("정렬"):
    sorted(range(500_000), reverse=True)

# 예외 발생해도 시간 출력
try:
    with timer("실패할 작업"):
        time.sleep(0.05)
        raise RuntimeError("실패")
except RuntimeError as e:
    print("바깥에서 잡음:", e)
