import os
from tkinter import filedialog
from rich.console import Console


#Prompt for a file name
def choose_file_name(class_num):
    console = Console()
    file_name = f"reading{class_num}.md"
    console.print(f"\nThe default name for your file will be: {file_name}. Would you like to choose a different file name? (y/n): ", style="bold yellow")
    file_name_choice = input("> ")

    if file_name_choice.lower() in ["y", "yes"]:
        file_name = input("Enter the file name: ")
        console.print(f"You have chosen file name {file_name}. Would you like to change this? (y/n):", style="bold green")
        confirm_choice = input("> ")
        if confirm_choice.lower() in ["y", "yes"]:
            choose_file_name(class_num)
        elif confirm_choice.lower() in ["n", "no"]:
            console.print(f"Ok! Your file name will be {file_name}.", style="bold green")
        else:
            console.print("Response not recognized. Returning to file name prompt.", style="bold red")
            choose_file_name(class_num)

    elif file_name_choice.lower() in ["n", "no"]:
        console.print(f"Ok! Your file name will remain {file_name}.", style="bold green")

    else:
        console.print("Response not recognized. Returning to file name prompt.", style="bold red")
        choose_file_name(class_num)
    
    return file_name
