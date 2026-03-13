from rich import print
from rich.console import Console
from rich.table import Table
import time

console = Console()

def banner():
    print(r"""
 _______  ___________________    _______      __________________     _____    _______   
 \      \ \_   _____/\_____  \   \      \    /   _____/\_   ___ \   /  _  \   \      \  
 /   |   \ |    __)_  /   |   \  /   |   \   \_____  \ /    \  \/  /  /_\  \  /   |   \ 
/    |    \|        \/    |    \/    |    \  /        \\     \____/    |    \/    |    \
\____|__  /_______  /\_______  /\____|__  / /_______  / \______  /\____|__  /\____|__  /
        \/        \/         \/         \/          \/         \/         \/         \/ 
    """)

#def banner():
 #   console.print("[bold magenta]\nNEONSCAN — Port Scanner\n[/bold magenta]")

def show_results(results):
    table = Table(title="Scan Results", style="magenta")
    table.add_column("IP")
    table.add_column("Open Ports")

    for ip, ports in results.items():
        if ports:
            table.add_row(ip, f"[green]{ports}[/green]")
        else:
            table.add_row(ip, "[red]None[/red]")

    console.print(table)

def shutdown_message():
    console.print("\n[bold magenta]Shutting down...[/bold magenta]")
    time.sleep(1)
