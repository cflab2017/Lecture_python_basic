import threading

counter_unsafe = 0
counter_safe = 0
lock = threading.Lock()

def inc_unsafe():
    global counter_unsafe
    for _ in range(100_000):
        counter_unsafe += 1

def inc_safe():
    global counter_safe
    for _ in range(100_000):
        with lock:
            counter_safe += 1

threads = []
for fn in [inc_unsafe] * 4:
    t = threading.Thread(target=fn); t.start(); threads.append(t)
for t in threads: t.join()

threads = []
for fn in [inc_safe] * 4:
    t = threading.Thread(target=fn); t.start(); threads.append(t)
for t in threads: t.join()

print(f"Lock 없이: {counter_unsafe} (기대 400000, 실제 더 작을 가능성)")
print(f"Lock 사용: {counter_safe}")
