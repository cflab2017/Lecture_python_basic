from datetime import datetime
from pathlib import Path

NOTES = Path("notes.txt")

while True:
    cmd = input("\n명령(add/show/clear/quit): ").strip()
    if cmd == "quit":
        break
    elif cmd == "add":
        memo = input("메모: ")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        with NOTES.open("a", encoding="utf-8") as f:
            f.write(f"[{ts}] {memo}\n")
        print("추가됨")
    elif cmd == "show":
        if NOTES.exists():
            print(NOTES.read_text(encoding="utf-8"))
        else:
            print("(메모 없음)")
    elif cmd == "clear":
        NOTES.write_text("", encoding="utf-8")
        print("비웠습니다")
