import os
from tkinter import filedialog
from rich.console import Console


def choose_file_name(class_num):
    """
    Prompt the user to choose a file name for the reading file.

    Args:
        class_num (str): The class number associated with the reading assignment.

    Returns:
        str: The chosen file name.
    """
    console = Console()
    file_name = f"reading{class_num}.md"
    
    console.print(f"\nThe default name for your file will be '{file_name}'. Would you like to choose a different file name? (y/n): ", style="bold yellow")
    file_name_choice = input("> ")

    if file_name_choice.lower() in ["n", "no"]:
        console.print(f"Ok! Your file name will remain '{file_name}'.", style="bold green")

    elif file_name_choice.lower() in ["y", "yes"]:
        file_name = input("Your file name must end in '.md'. Please enter your file name: ")
        if not file_name.endswith(".md"):
            console.print("Oops! Invalid file name. Your file name must end with '.md'. Returning to the file name prompt.", style="bold red")
            return choose_file_name(class_num)
        else:
            console.print(f"Ok! Your file name is '{file_name}'.")

    else:
        console.print("Response not recognized. Returning to the file name prompt.", style="bold red")
        return choose_file_name(class_num)
    
    return file_name
