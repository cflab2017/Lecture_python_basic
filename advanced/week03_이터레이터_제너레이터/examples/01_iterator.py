class Range:
    def __init__(self, start, stop):
        self.cur = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= self.stop:
            raise StopIteration
        self.cur += 1
        return self.cur - 1

print(list(Range(1, 5)))

# for 문은 사실 이렇게 동작
r = Range(1, 4)
it = iter(r)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
