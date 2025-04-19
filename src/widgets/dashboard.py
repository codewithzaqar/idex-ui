from textual.widget import Widget
from textual.reactive import reactive
from src.utils.system_info import get_system_info
from rich.panel import Panel
from rich.text import Text
import asyncio

class Dashboard(Widget):
    """Dashboard widget displaying system information."""
    info = reactive({"cpu": 0.0, "memory": 0.0, "disk": 0.0})

    def on_mount(self) -> None:
        """Start updating system info."""
        self.set_interval(2.0, self.update_info)

    async def update_info(self) -> None:
        """Fetch and update system information."""
        self.info = get_system_info()
        self.refresh()

    def render(self) -> Panel:
        """Render this dashboard."""
        cpu_text = Text(f"CPU Usage: {self.info['cpu']:.1f}%", style="cyan")
        mem_text = Text(f"Memory: {self.info['memory']:.1f}%", style="magenta")
        disk_text = Text(f"Disk: {self.info['disk']:.1f}%", style="yellow")
        content = Text.assemble(cpu_text, "\n", mem_text, "\n", disk_text)
        return Panel(content, title="System Monitor", border_style="green")