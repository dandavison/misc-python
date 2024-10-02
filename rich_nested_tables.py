from rich.console import Console
from rich.table import Table

console = Console()

t1 = Table(show_header=False)
t1.add_row("myrow", "myval")

t2 = Table(show_header=False)
t2.add_row("myrow", t1)


console.print(t2)
