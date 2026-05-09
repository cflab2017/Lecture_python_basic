from pathlib import Path

folder = Path(input("폴더 경로: ").strip() or ".")
files = sorted(folder.glob("*.txt"), key=lambda p: -p.stat().st_size)

total = 0
for f in files:
    size = f.stat().st_size
    total += size
    print(f"{f.name:20} {size:>8,} bytes")
print(f"총 {len(files)}개 파일, {total:,} bytes")
