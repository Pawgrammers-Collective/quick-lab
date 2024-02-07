import subprocess
from rich.table import Table
from rich.console import Console
import platform
import os

def create_pip_install(dependencies, directory):
    """
    Install pip dependencies and creates .venv/requirements.txt.

    Args:
        dependencies (list): List of pip dependencies to install.
        directory (str): Directory to install dependencies and create requirements.txt.
    """
    # checks pc
    pc_type = platform.system()

    # creates .venv file into the new directory
    subprocess.run(["python3", "-m", "venv", ".venv"], cwd=directory)

    if pc_type == "Darwin":

         # Install dependencies
        for dependency in dependencies:
            subprocess.run([f'{directory}/.venv/bin/pip', 'install', dependency], cwd=directory, text=True)
        
        # grabs the requirements
        result = subprocess.run([f'{directory}/.venv/bin/pip', 'freeze', '>', f'{directory}/requirements.txt'], cwd=directory, capture_output=True, text=True)

        # Creates a requirements.txt and writes the dependencies within
        with open(f'{directory}/requirements.txt', 'w') as gitignore:
            gitignore.write(result.stdout)

        
    
    # creates a .venv if the user is on pc.
    elif pc_type == "Windows":  

        # Installs the dependencies
        for dependency in dependencies:
            subprocess.run([f'{directory}/.venv/Scripts/pip', 'install', dependency], cwd=directory, text=True)

        # grabs the requirements
        result = subprocess.run([f'{directory}/.venv/Scripts/pip', 'freeze', '>', f'{directory}/requirements.txt'], cwd=directory, capture_output=True, text=True)

        # Creates a requirements and writes the dependencies within
        with open(f'{directory}/requirements.txt', 'w') as gitignore:
            gitignore.write(result.stdout)

    return os.path.exists(f"{directory}/.venv")




def display_pip_installs(pip_installs):
    """
    Display a table of pip installs.

    Args:
        pip_installs (list): List of pip installs.
    """
    # Create a new table
    table = Table(title="Pip Installs")
    table.add_column("#", style="dim")
    table.add_column("Dependency")

    # Add rows to the table
    for i, dep in enumerate(pip_installs):
        table.add_row(str(i+1), dep)

    # Print the table
    console = Console()
    console.clear()
    console.print(table)
