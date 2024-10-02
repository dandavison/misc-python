from textual.app import App, ComposeResult
from textual.widgets import ListItem, ListView, Static


class ListViewExample(App):
    CSS = """
    ListItem.highlighted {
        border: green;
    }
    """

    def compose(self) -> ComposeResult:
        yield ListView(*[ListItem(Static(f"Item {i}")) for i in range(1, 2 + 1)])

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if item := event.item:
            for other_item in self.query(ListItem):
                other_item.remove_class("highlighted")
            item.add_class("highlighted")


if __name__ == "__main__":
    app = ListViewExample()
    app.run()
