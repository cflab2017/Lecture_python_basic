"""일기장 — 날짜별 파일"""
from pathlib import Path
from datetime import date

DIARY = Path("diary")
DIARY.mkdir(exist_ok=True)

def write_today():
    today = date.today().isoformat()
    f = DIARY / f"{today}.txt"
    if f.exists():
        if input(f"{today} 이미 있음. 덮어쓸까? (y/n): ").lower() != "y":
            return
    print("내용 입력 (빈 줄 두 번이면 종료):")
    lines = []
    blank = 0
    while True:
        line = input()
        if line == "":
            blank += 1
            if blank >= 2: break
            lines.append("")
        else:
            blank = 0
            lines.append(line)
    f.write_text("\n".join(lines), encoding="utf-8")
    print(f"저장됨 ({f})")

def read(date_str):
    f = DIARY / f"{date_str}.txt"
    if not f.exists():
        print("없음"); return
    print(f.read_text(encoding="utf-8"))

def list_all():
    files = sorted(DIARY.glob("*.txt"))
    for f in files:
        size = len(f.read_text(encoding="utf-8"))
        print(f"  {f.stem} ({size}자)")
    print(f"\n총 {len(files)}일")

def search(keyword):
    for f in sorted(DIARY.glob("*.txt")):
        text = f.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if keyword in line:
                print(f"[{f.stem} L{i}] {line}")

def main():
    while True:
        raw = input("\n명령(write/read <date>/list/search <q>/quit): ").strip()
        if not raw: continue
        if raw == "quit": break
        parts = raw.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ""
        if cmd == "write": write_today()
        elif cmd == "read":
            read(arg if arg else date.today().isoformat())
        elif cmd == "list": list_all()
        elif cmd == "search":
            if arg: search(arg)

if __name__ == "__main__":
    main()
