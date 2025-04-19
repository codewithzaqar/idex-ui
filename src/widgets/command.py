from textual.widgets import Input
from textual.reactive import reactive
from rich.panel import Panel
import os
import getpass

class CommandInput(Input):
    """Command input widget with basic execution."""
    output = reactive("")

    def render(self) -> Panel:
        """Render the command input with output."""
        input_text = f"> {self.value}"
        content = f"{self.output}\n{input_text}" if self.output else input_text
        return Panel(content, title="Command", border_style="red")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle command submission."""
        command = event.value.strip()
        self.value = ""
        self.output = self.execute_command(command)
        self.refresh()

    def execute_command(self, command: str) -> str:
        """Execute a command and return output."""
        if not command:
            return ""
        if command == "clear":
            return ""
        elif command == "whoami":
            return getpass.getuser()
        elif command.startswith("echo "):
            return command[5:].strip()
        else:
            return f"Command '{command}' not recognized."