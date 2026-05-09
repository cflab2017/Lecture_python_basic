import json
from pathlib import Path

DB = Path("todos.json")

def load():
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8"))
    return []

def save(todos):
    DB.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")

todos = load()
print(f"불러온 할 일 {len(todos)}개")

while True:
    cmd = input("\n명령(add/list/done <n>/quit): ").strip()
    if cmd == "quit":
        save(todos)
        break
    if cmd == "add":
        task = input("할 일: ")
        todos.append({"task": task, "done": False})
        save(todos)
    elif cmd == "list":
        for i, t in enumerate(todos, 1):
            mark = "[x]" if t["done"] else "[ ]"
            print(f"{i}. {mark} {t['task']}")
    elif cmd.startswith("done "):
        idx = int(cmd.split()[1]) - 1
        if 0 <= idx < len(todos):
            todos[idx]["done"] = True
            save(todos)
