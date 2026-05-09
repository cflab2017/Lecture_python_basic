def chain(*iters):
    for it in iters:
        yield from it

print(list(chain([1, 2], (3, 4), "ab")))

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # 재귀
        else:
            yield item

print(list(flatten([1, [2, [3, [4, 5]]], 6])))
