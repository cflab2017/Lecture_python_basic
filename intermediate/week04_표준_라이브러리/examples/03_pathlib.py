from pathlib import Path

# 경로 조합
p = Path("data") / "report" / "summary.txt"
print(p)

# 부모 폴더 생성
p.parent.mkdir(parents=True, exist_ok=True)

# 쓰기/읽기
p.write_text("안녕하세요\n파이썬!", encoding="utf-8")
print(p.read_text(encoding="utf-8"))

# 정보
print("존재:", p.exists())
print("이름:", p.name)
print("확장자:", p.suffix)
print("이름(확장자 빼고):", p.stem)
print("크기:", p.stat().st_size)

# 폴더 순회
for f in Path(".").glob("*.py"):
    print(f.name)
