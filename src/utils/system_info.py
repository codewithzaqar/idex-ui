import psutil

def get_system_info() -> dict:
    """Fetch system information (CPU, memory, and disk usage)."""
    cpu = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage(".").percent
    return {"cpu": cpu, "memory": memory, "disk": disk}