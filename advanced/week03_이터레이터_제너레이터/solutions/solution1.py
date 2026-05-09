from pathlib import Path

def chunked_lines(path, n):
    chunk = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            chunk.append(line.rstrip())
            if len(chunk) >= n:
                yield chunk
                chunk = []
    if chunk:
        yield chunk

# 데모: 자기 자신을 3줄씩
self_path = Path(__file__)
for i, chunk in enumerate(chunked_lines(self_path, 3), 1):
    print(f"--- chunk {i} ---")
    for line in chunk:
        print(line)
