"""argparse 기반 To-Do CLI"""
import argparse
import json
from pathlib import Path

DB = Path("todos_cli.json")

def load():
    return json.loads(DB.read_text(encoding="utf-8")) if DB.exists() else []

def save(items):
    DB.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

def cmd_add(args):
    items = load()
    items.append({
        "id": len(items) + 1,
        "task": args.task,
        "priority": args.priority,
        "done": False,
    })
    save(items)
    print(f"추가됨 #{items[-1]['id']}: {args.task}")

def cmd_list(args):
    items = load()
    if args.only_pending:
        items = [i for i in items if not i["done"]]
    if not items:
        print("(비어있음)"); return
    for it in items:
        mark = "[x]" if it["done"] else "[ ]"
        print(f"{it['id']:>3}. {mark}[{it['priority']}] {it['task']}")

def cmd_done(args):
    items = load()
    for it in items:
        if it["id"] == args.id:
            it["done"] = True
            save(items)
            print(f"#{args.id} 완료")
            return
    print(f"#{args.id} 없음")

def cmd_del(args):
    items = load()
    new_items = [i for i in items if i["id"] != args.id]
    if len(new_items) == len(items):
        print(f"#{args.id} 없음"); return
    save(new_items)
    print(f"#{args.id} 삭제")

def build_parser():
    p = argparse.ArgumentParser(prog="todo")
    p.add_argument("--version", action="version", version="todo 1.0.0")
    sub = p.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add")
    add.add_argument("task")
    add.add_argument("--priority", choices=["low", "high"], default="low")
    add.set_defaults(func=cmd_add)

    lst = sub.add_parser("list")
    lst.add_argument("--only-pending", action="store_true")
    lst.set_defaults(func=cmd_list)

    done = sub.add_parser("done")
    done.add_argument("id", type=int)
    done.set_defaults(func=cmd_done)

    delcmd = sub.add_parser("del")
    delcmd.add_argument("id", type=int)
    delcmd.set_defaults(func=cmd_del)

    return p

def main():
    args = build_parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
