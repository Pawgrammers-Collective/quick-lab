from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os


def menu():
    console = Console()
    while True:
        console.print("\n1. [bold green]Create Lab Repo[/bold green]\n2. [bold blue]Create Reading Assignment[/bold blue]\n3. [bold red]Exit[/bold red]")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3'], default='3')

        if choice == '1':
            return
        elif choice == '2':
            class_num = Prompt.ask("Which class number would you like to create a reading assignment for?")
            return class_num
        else:
            break