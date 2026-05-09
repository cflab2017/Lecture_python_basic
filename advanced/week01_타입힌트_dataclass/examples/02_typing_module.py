from typing import Optional, Union, Any, Callable

def find_user(uid: int) -> Optional[dict]:
    if uid == 1:
        return {"name": "Alice"}
    return None

def parse_int(value: Union[str, int]) -> int:
    return int(value)

# Python 3.10+ 신문법
def find_user2(uid: int) -> dict | None:
    if uid == 1:
        return {"name": "Alice"}
    return None

def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

print(find_user(1))
print(find_user(99))
print(parse_int("42"))
print(apply(lambda n: n * 2, 5))
