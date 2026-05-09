class FileLock:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        print(f"잠금 획득: {self.path}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"잠금 해제: {self.path}")
        if exc:
            print(f"  예외 발생: {exc}")
        return False    # False면 예외를 그대로 전파

with FileLock("data.txt"):
    print("작업 중")

print("---")

try:
    with FileLock("data.txt"):
        raise ValueError("의도적 에러")
except ValueError as e:
    print("바깥에서 잡음:", e)
