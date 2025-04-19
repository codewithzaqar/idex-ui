from textual.widget import Widget
from rich.panel import Panel
from rich.text import Text
import os

class FileExplorer(Widget):
    """File explorer widget displaying directory contents."""
    
    def render(self) -> Panel:
        """Render the file explorer."""
        files = os.listdir(".")
        content = Text("\n".join(files), style="white")
        return Panel(content, title="File Explorer", border_style="magenta")