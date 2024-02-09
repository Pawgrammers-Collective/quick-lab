import webbrowser
from rich.console import Console

console = Console()

def surprise_me():
    console.print("You have unlocked the best easter egg. Enjoy!", style="bold green")
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)
    