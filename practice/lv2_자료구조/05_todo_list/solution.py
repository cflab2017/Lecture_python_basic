"""To-Do List — 우선순위·마감일 지원"""

PRIORITY_ORDER = {"높음": 0, "보통": 1, "낮음": 2}
todos = []

def add():
    task = input("할 일: ").strip()
    if not task: return
    p = input("우선순위 (높음/보통/낮음, 기본 보통): ").strip() or "보통"
    if p not in PRIORITY_ORDER:
        p = "보통"
    due = input("마감일 (YYYY-MM-DD, 없으면 엔터): ").strip()
    todos.append({"task": task, "done": False, "priority": p, "due": due})
    print("추가됨")

def show(args=""):
    items = list(enumerate(todos, 1))
    if "--pending" in args:
        items = [(i, t) for i, t in items if not t["done"]]
    if "--sort priority" in args:
        items.sort(key=lambda x: PRIORITY_ORDER[x[1]["priority"]])
    if not items:
        print("(비어있음)"); return
    for i, t in items:
        mark = "[x]" if t["done"] else "[ ]"
        due = f"~{t['due']}" if t["due"] else ""
        print(f"{i}. {mark}[{t['priority']}] {t['task']} {due}".rstrip())

def main():
    while True:
        raw = input("\n> ").strip()
        if not raw: continue
        parts = raw.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ""
        if cmd == "quit": break
        elif cmd == "add": add()
        elif cmd == "list": show(arg)
        elif cmd == "done":
            try:
                idx = int(arg) - 1
                if 0 <= idx < len(todos):
                    todos[idx]["done"] = True
                    print("완료")
                else:
                    print("번호 없음")
            except ValueError:
                print("번호를 입력하세요")
        elif cmd == "del":
            try:
                idx = int(arg) - 1
                if 0 <= idx < len(todos):
                    del todos[idx]
                    print("삭제")
            except ValueError:
                print("번호를 입력하세요")
        else:
            print("알 수 없는 명령")

if __name__ == "__main__":
    main()
