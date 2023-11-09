import time
from rich.progress import track

for i in track(range(20), description="[purple]Rodando", style='black', complete_style='white', finished_style='green'):
    time.sleep(1)  # Simulate work being 
    