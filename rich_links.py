from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

table = Table(show_header=False)
table.add_row("Key", "I am wide I am wide I am wide")
table.add_row("Key", Text("Value", style="link http://example.com"))
table.add_row("Key", "[link=http://example.com]Value[/link]")
console.print(table)
