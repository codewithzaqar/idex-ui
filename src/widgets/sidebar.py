from textual.widget import Widget
from textual.message import Message
from rich.panel import Panel
from rich.text import Text

class Sidebar(Widget):
    """Interactive sidebar widget for navigation."""
    class MenuSelected(Message):
        """Message sent when a menu item is selected."""
        def __init__(self, selection: str):
            self.selection = selection
            super().__init__()

    selected = 0
    options = ["Dashboard", "File Explorer", "Network", "Settings"]

    def render(self) -> Panel:
        """Render the sidebar."""
        menu = []
        for i, option in enumerate(self.options):
            style = "bold white on blue" if i == self.selected else "yellow"
            menu.append(Text(f"{i+1}. {option}", style=style))
        content = Text("\n".join(str(item) for item in menu))
        return Panel(content, title="Menu", border_style="blue")
    
    def on_key(self, event) -> None:
        """Handle key presses for menu navigation."""
        if event.key == "up" and self.selected > 0:
            self.selected -= 1
            self.refresh()
        elif event.key == "down" and self.selected < len(self.options) - 1:
            self.selected += 1
            self.refresh()
        elif event.key == "enter":
            selection = self.options[self.selected].lower().replace(" ", "")
            self.post_message(self.MenuSelected(selection))