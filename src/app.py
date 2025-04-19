from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from src.widgets.dashboard import Dashboard
from src.widgets.sidebar import Sidebar
from src.widgets.command import CommandInput

class IDEXApp(App):
    """iDEX-UI inspired CLI application."""
    CSS = """
    Screen {
        background: #0a0e14;
        color: #b3b9c5;
    }
    Dashboard {
        width: 3fr;
        height: 100%;
    }
    Sidebar {
        width: 1fr;
        height: 100%;
        background: #1c2526;
    }
    CommandInput {
        dock: bottom;
        height: 3;
        background: #1c2526;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the main layout."""
        yield Horizontal(
            Sidebar(),
            Dashboard(),
        )
        yield CommandInput()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.title = "iDEX-CLI v0.01"