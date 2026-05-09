import os

# 임시 파일
TMP = "tmp_demo.txt"
with open(TMP, "w") as f:
    f.write("hello\n안녕\n")

try:
    f = open(TMP, encoding="utf-8")
except FileNotFoundError:
    print("파일 없음")
else:
    print("내용:", f.read())
    f.close()
finally:
    print("정리 중")
    os.remove(TMP)
