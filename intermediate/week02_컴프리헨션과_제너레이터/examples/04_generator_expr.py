import sys

# 리스트 컴프리헨션 — 메모리 다 잡아먹음
list_sq = [x * x for x in range(1_000_000)]
print(f"list 메모리: {sys.getsizeof(list_sq):,} bytes")

# 제너레이터 표현식 — 한 번에 하나씩
gen_sq = (x * x for x in range(1_000_000))
print(f"generator 메모리: {sys.getsizeof(gen_sq):,} bytes")

# 결과는 동일
print(sum(x * x for x in range(100)))
