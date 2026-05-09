from functools import wraps
from datetime import datetime
from pathlib import Path

LOG = Path("app.log")

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        args_str = ", ".join(repr(a) for a in args)
        kw_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kw_str]))
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"{ts} {func.__name__}({all_args}) -> {result!r}\n")
        return result
    return wrapper

@logged
def add(a, b):
    return a + b

@logged
def greet(name, greeting="안녕"):
    return f"{greeting}, {name}"

print(add(3, 5))
print(greet("홍길동"))
print(greet("Alice", greeting="Hello"))
print("로그:")
print(LOG.read_text(encoding="utf-8"))

LOG.unlink()
