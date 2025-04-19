from textual.widgets import Input
from textual.reactive import reactive
from rich.panel import Panel

class CommandInput(Input):
    """Command input widget."""
    command = reactive("")

    def render(self) -> Panel:
        """Render the command input."""
        return Panel(
            self._render_input(),
            title="Command",
            border_style="red"
        )
    
    def _render_input(self) -> str:
        """Render the input field."""
        return f"> {self.value}"