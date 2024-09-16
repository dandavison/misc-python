import webbrowser

from rich.table import Table
from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Markdown, Static


def make_table() -> Table:
    url = "http://example.com"
    table = Table(show_header=False)
    table.add_row(f"[link={url}]I am a link[/link]")
    table.add_row(f"[@click=app.webbrowser('{url}')]I am a link[/]")
    return table


class MyWidget(Widget):
    def render(self) -> RenderResult:
        return make_table()


class MyMarkdownWidget(Markdown):
    def render(self) -> RenderResult:
        return "[hello](http://example.com)"


class MyWebLink(Static):
    def render(self) -> RenderResult:
        url = "http://example.com"
        return f"[@click=app.webbrowser('{url}')]I am a link[/]"


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield MyWebLink()

    def action_webbrowser(self, url: str):
        webbrowser.open(url)


if True:
    MyApp().run()
else:
    from rich.console import Console

    console = Console()
    console.print(make_table())
