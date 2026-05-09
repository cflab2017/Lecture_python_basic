"""CSV 자동 분석 — 표준 csv 모듈만 사용"""
import csv
import sys
from collections import Counter
from pathlib import Path

def is_number(s):
    try:
        float(s); return True
    except ValueError:
        return False

def analyze(path):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        cols = reader.fieldnames

    if not rows:
        return ["(빈 파일)"]

    out = [f"[행 수] {len(rows)}"]

    for col in cols:
        values = [r[col] for r in rows if r[col] != ""]
        if not values: continue

        if all(is_number(v) for v in values):
            nums = [float(v) for v in values]
            out.append(f"\n[숫자: {col}]")
            out.append(f"  평균: {sum(nums) / len(nums):,.2f}")
            out.append(f"  최대: {max(nums):,.2f}")
            out.append(f"  최소: {min(nums):,.2f}")
            out.append(f"  합계: {sum(nums):,.2f}")
        else:
            counter = Counter(values)
            out.append(f"\n[문자: {col}]")
            for val, cnt in counter.most_common(5):
                out.append(f"  {val:<20} {cnt:>6}")

    return out

def main():
    if len(sys.argv) != 2:
        print("사용법: python solution.py <csv 파일>")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"파일 없음: {path}")
        sys.exit(1)

    result = analyze(path)
    text = "\n".join(result)
    print(text)
    Path("report.txt").write_text(text, encoding="utf-8")
    print("\nreport.txt 저장됨")

if __name__ == "__main__":
    main()
