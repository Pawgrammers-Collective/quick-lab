import os
from tkinter import filedialog
from rich.console import Console


#Prompt for a file name
def choose_file_name(class_num):
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
            choose_file_name(class_num)
        else:
            console.print(f"You have chosen file name '{file_name}'. Please enter 'y' to confirm this is the file name you would like to use. Enter 'n' to change it (y/n):", style="bold green")
            confirm_choice = input("> ")
            if confirm_choice.lower() in ["y", "yes"]:
                console.print(f"Ok! Your file name will be '{file_name}'.", style="bold green")
            elif confirm_choice.lower() in ["n", "no"]:
                console.print("Ok! Returning to the file name prompt.", style="bold yellow")
                choose_file_name(class_num)
            else:
                console.print("Response not recognized. Returning to the file name prompt.", style="bold red")
                choose_file_name(class_num)

    else:
        console.print("Response not recognized. Returning to the file name prompt.", style="bold red")
        choose_file_name(class_num)
    
    return file_name
