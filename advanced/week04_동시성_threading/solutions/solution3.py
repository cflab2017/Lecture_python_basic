import threading

def run(use_lock):
    counter = 0
    lock = threading.Lock()

    def inc():
        nonlocal counter
        if use_lock:
            for _ in range(10_000):
                with lock:
                    counter += 1
        else:
            for _ in range(10_000):
                counter += 1

    threads = [threading.Thread(target=inc) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()
    return counter

print(f"Lock 없이: {run(False)} (기대 40000)")
print(f"Lock 사용: {run(True)}")
print("→ Lock 없으면 race condition 발생 가능")
