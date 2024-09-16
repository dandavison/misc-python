from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.css.query import NoMatches
from textual.widgets import Collapsible, ListItem, ListView, Static
from textual.widgets._collapsible import CollapsibleTitle


class CollapsibleContent(Static):
    def __init__(self, i: int):
        super().__init__()
        self.i = i

    def render(self) -> str:
        return f"content {self.i}."


class ListViewCollapsibleExample(App):
    CSS_PATH = "textual_listview_collapsible.tcss"

    BINDINGS = [
        Binding("right", "show_test_output", "Show test output"),
        Binding("left", "hide_test_output", "Hide test output"),
    ]

    def compose(self) -> ComposeResult:
        yield ListView(
            *[
                ListItem(Collapsible(CollapsibleContent(i), title=f"Item {i}"))
                for i in range(1, 6)
            ]
        )

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if item := event.item:
            if title := item.query_one(CollapsibleTitle):
                for other_title in self.query(CollapsibleTitle):
                    other_title.remove_class("highlighted")
                title.add_class("highlighted")

    def action_show_test_output(self) -> None:
        self._set_test_output_visible(True)

    def action_hide_test_output(self) -> None:
        self._set_test_output_visible(False)

    def _set_test_output_visible(self, visible: bool) -> None:
        if focused := self.focused:
            if isinstance(focused, ListView):
                if list_item := focused.highlighted_child:
                    try:
                        collapsible = list_item.query_one(Collapsible)
                    except NoMatches:
                        pass
                    else:
                        collapsible.collapsed = not visible


if __name__ == "__main__":
    app = ListViewCollapsibleExample()
    app.run()
