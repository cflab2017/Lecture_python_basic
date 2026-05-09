# 쓰기
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("첫 줄\n")
    f.write("둘째 줄\n")
    f.writelines(["A\n", "B\n", "C\n"])

# 읽기 — 전체
with open("notes.txt", encoding="utf-8") as f:
    print(f.read())

print("---")

# 읽기 — 한 줄씩
with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(repr(line.rstrip()))

# 추가 모드
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("추가된 줄\n")

import os
os.remove("notes.txt")
