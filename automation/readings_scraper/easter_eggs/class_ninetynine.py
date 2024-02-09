import shutil
import tkinter
import os
from tkinter import filedialog
from rich.console import Console


console = Console()

def class_ninetynine():
    """
    Create a class 99 image file.

    This function is called when the user chooses class 99. It prepares for rain by creating a file named "class99.png" 
    and copies an image file named "class99.png" from the assets folder to the chosen directory.

    Returns:
        None
    """
    console.print("You have chosen class 99. Prepare for rain.", style="dark_magenta")
    file_name = "class99.png"
    root = tkinter.Tk()
    directory = filedialog.askdirectory(title="Choose the folder for your class99 file", parent=root)
    root.withdraw()
    file_path = os.path.join(f'{directory}/{file_name}')
    
    if not file_path:
        return

    shutil.copy("assets/class99.png", file_path)
    console.print('File 99 created successfully! Party like it\'s...', style="bold purple")
