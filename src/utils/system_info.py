import psutil

def get_system_info() -> dict:
    """Fetch system information (CPU and memory usage)."""
    cpu = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory().percent
    return {"cpu": cpu, "memory": memory}