from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from src.widgets.dashboard import Dashboard
from src.widgets.sidebar import Sidebar
from src.widgets.command import CommandInput
from src.widgets.file_explorer import FileExplorer

class IDEXApp(App):
    """iDEX-UI inspired CLI application."""
    CSS = """
    Screen {
        background: #0a0e14;
        color: #b3b9c5;
        layout: grid;
        grid-size: 4 2;
        grid-gutter: 1;
    }
    Dashboard {
        column-span: 3;
        row-span: 1;
        background: #1c2526;
        border: tall #00ff87;
    }
    Sidebar {
        width: 1fr;
        column-span: 1;
        row-span: 2;
        background: #1c2526;
        border: tall #00d4ff;
    }
    FileExplorer {
        column-span: 3;
        row-span: 1;
        background: #1c2526;
        border: tall #ff00ff;
    }
    CommandInput {
        column-span: 4;
        height: 3;
        background: #1c2526;
        border: tall #ff4500;
    }
    """

    active_widget = reactive("dashboard")

    def compose(self) -> ComposeResult:
        """Compose the main layout."""
        yield Sidebar()
        yield Dashboard()
        yield FileExplorer()
        yield CommandInput()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.title = "iDEX-CLI v0.02"
        self.query_one(FileExplorer).visible = False

    def on_sidebar_menu_selected(self, event: Sidebar.MenuSelected) -> None:
        """Handle sidebar menu selection."""
        self.active_widget = event.selection
        dashboard = self.query_one(Dashboard)
        explorer = self.query_one(FileExplorer)
        dashboard.visible = self.active_widget == "dashboard"
        explorer.visible = self.active_widget == "explorer"