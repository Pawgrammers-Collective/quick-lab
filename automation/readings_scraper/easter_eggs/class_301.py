import webbrowser
from rich.console import Console

console = Console()

def class_301():
    console.print("You have unlocked the Code Fellows 301 easter egg. See our 301 project!", style="bold green")
    url = "https://jobdotfetch.netlify.app/"
    webbrowser.open(url)
