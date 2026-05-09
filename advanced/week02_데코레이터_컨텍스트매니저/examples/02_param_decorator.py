import random
from functools import wraps

def retry(times):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"재시도 {i+1}/{times}: {e}")
            raise RuntimeError(f"{times}회 실패")
        return wrapper
    return deco

@retry(3)
def fragile():
    if random.random() < 0.7:
        raise ValueError("일시적 오류")
    return "성공"

print(fragile())
