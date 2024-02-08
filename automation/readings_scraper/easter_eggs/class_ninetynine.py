import shutil
from rich.console import Console
from automation.readings_scraper.choose_directory import choose_directory


console = Console()

def class_ninetynine():
    console.print("You have chosen class 99. Prepare for rain.", style="dark_magenta")
    file_name = "class99.png"
    file_path = choose_directory(file_name)
    if not file_path:
        return

    shutil.copy("assets/class99.png", file_path)
    console.print('File 99 created successfully! Party like it\'s...', style="bold purple")
    