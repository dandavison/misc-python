from rich.console import Console
from rich.table import Table

console = Console()

t1 = Table(title="My Table", show_header=False)
t1.add_row(
    "myrow",
    "\n".join(
        [f"[link=http://example.com?i={i} ]myval{i}[/link]" for i in range(1, 3 + 1)]
    ),
)

t2 = Table(show_header=False)
t2.add_row("myrow", t1)


console.print(t2)
