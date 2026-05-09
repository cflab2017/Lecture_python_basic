def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5, 6))

def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(name="홍길동", age=20, city="서울")

def log(prefix, *args, **kwargs):
    print(f"[{prefix}]", args, kwargs)

log("INFO", 1, 2, 3, user="alice", level=2)
