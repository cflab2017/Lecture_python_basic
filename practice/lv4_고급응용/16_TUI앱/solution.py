"""TUI To-Do (rich) — pip install rich

rich 가 없으면 graceful 하게 폴백.
"""

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

todos = [
    {"id": 1, "task": "우유 사기", "priority": "보통", "done": False},
    {"id": 2, "task": "책 반납", "priority": "높음", "done": True},
    {"id": 3, "task": "운동", "priority": "낮음", "done": False},
]

PRIORITY_STYLE = {"높음": "red", "보통": "yellow", "낮음": "green"}

def render_rich():
    console = Console()
    table = Table(title="📋 My To-Do", show_lines=True, header_style="bold cyan")
    table.add_column("번호", justify="right", style="cyan")
    table.add_column("상태", justify="center")
    table.add_column("우선순위", justify="center")
    table.add_column("할 일")
    for t in todos:
        mark = "[green]✓ 완료[/]" if t["done"] else "[yellow]○ 진행[/]"
        prio = f"[{PRIORITY_STYLE[t['priority']]}]{t['priority']}[/]"
        task = f"[strike]{t['task']}[/]" if t["done"] else t["task"]
        table.add_row(str(t["id"]), mark, prio, task)
    console.print(table)
    pending = sum(1 for t in todos if not t["done"])
    console.print(Panel(f"미완료: [bold red]{pending}[/]개  /  전체 {len(todos)}개", style="dim"))

def render_plain():
    print("📋 My To-Do (plain mode — pip install rich 권장)")
    for t in todos:
        mark = "[x]" if t["done"] else "[ ]"
        print(f"  {t['id']}. {mark}[{t['priority']}] {t['task']}")

def main():
    if HAS_RICH:
        render_rich()
    else:
        print("⚠️ rich 미설치. plain 모드로 출력.")
        render_plain()

if __name__ == "__main__":
    main()
