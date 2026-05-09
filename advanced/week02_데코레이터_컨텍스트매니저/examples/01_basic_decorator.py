from functools import wraps

def loud(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f">>> {func.__name__} 호출 args={args}")
        result = func(*args, **kwargs)
        print(f"<<< 결과: {result}")
        return result
    return wrapper

@loud
def add(a, b):
    """두 수의 합"""
    return a + b

add(3, 5)
print(add.__name__, add.__doc__)   # 정상 유지
