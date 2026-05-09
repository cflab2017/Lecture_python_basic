from collections import Counter, defaultdict, deque

# Counter
text = "the quick brown fox jumps over the lazy dog the quick"
words = text.split()
c = Counter(words)
print(c)
print(c.most_common(3))

# defaultdict — 키가 없으면 자동 생성
groups = defaultdict(list)
for name, age in [("A", 20), ("B", 25), ("C", 20), ("D", 25)]:
    groups[age].append(name)
print(dict(groups))

# deque — 양쪽에서 빠른 추가/제거
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
dq.popleft()
dq.pop()
print(dq)
