from rich.table import Table
from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget


def make_table() -> Table:
    table = Table(show_header=False)
    table.add_row("[link=http://example.com]I am a link[/link]")
    return table


class MyWidget(Widget):
    def render(self) -> RenderResult:
        return make_table()


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield MyWidget()


if True:
    MyApp().run()
else:
    from rich.console import Console

    console = Console()
    console.print(make_table())
