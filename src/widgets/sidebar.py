from textual.widget import Widget
from rich.panel import Panel
from rich.text import Text

class Sidebar(Widget):
    """Sidebar widget for navigation."""

    def render(self) -> Panel:
        """Render the sidebar."""
        menu = Text("1. Dashboard\n2. Files\n3. Network\n4. Settings", style="yellow")
        return Panel(menu, title="Menu", border_style="blue")