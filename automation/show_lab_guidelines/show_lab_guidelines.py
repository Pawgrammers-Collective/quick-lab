import webbrowser
from rich.console import Console

console = Console()

def show_lab_guidelines():
    console.print("\nHere are the Lab Submission Guidelines \U0001F600", style="magenta")
    url = "https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/"
    webbrowser.open(url)
    