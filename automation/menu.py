from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os


def menu():
    console = Console()
    while True:
        console.print("\n1. Create Lab Repo\n2. Create Reading Assignment\n3. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3'], default='3')

        if choice == '1':
            directory = Prompt.ask("Enter the directory to list files")
            list_files(directory)
        elif choice == '2':
            directory = Prompt.ask("Enter the current directory of the file")
            file = Prompt.ask("Enter the file to move")
            target_directory = Prompt.ask("Enter the target directory to move the file to")
            move_file(directory, file, target_directory)
        elif choice == '3':
            directory = Prompt.ask("Enter the directory to search files")
            pattern = Prompt.ask("Enter the regex pattern to search for")
            search_files(directory, pattern)
        else:
            break