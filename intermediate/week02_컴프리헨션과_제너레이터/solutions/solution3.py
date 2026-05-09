def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield line

def chunked_lines(path, n):
    chunk = []
    for line in read_lines(path):
        chunk.append(line)
        if len(chunk) >= n:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

# 테스트용 (자체 파일을 읽기)
import sys, pathlib
self_path = pathlib.Path(__file__)
for line in read_lines(self_path):
    print(line)
print("---")
for chunk in chunked_lines(self_path, 3):
    print("청크:", chunk)
    print("---")
