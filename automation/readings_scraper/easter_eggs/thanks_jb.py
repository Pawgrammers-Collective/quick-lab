import shutil
import tkinter
import os
from tkinter import filedialog
from rich.console import Console


console = Console()

def thanks_jb():
    """
    Create a JB image file.

    Returns:
        None
    """
    console.print("Shout out to JB! Choose a location for your JB image file", style="magenta1")
    file_name = "thanks-JB.png"
    root = tkinter.Tk()
    directory = filedialog.askdirectory(title="Choose the folder for your 'thanks-JB' file", parent=root)
    root.withdraw()
    file_path = os.path.join(f'{directory}/{file_name}')

    if not file_path:
        return

    shutil.copy("assets/thanks-JB.png", file_path)
    console.print("Your 'thanks-JB' file created successfully!", style="magenta1")
