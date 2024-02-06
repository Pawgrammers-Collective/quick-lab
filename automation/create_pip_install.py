import subprocess
from rich.table import Table
from rich.console import Console

def create_pip_install(dependencies, directory):
    """
    Install pip dependencies and create requirements.txt.

    Args:
        dependencies (list): List of pip dependencies to install.
        directory (str): Directory to install dependencies and create requirements.txt.
    """

    # Install dependencies
    for dependency in dependencies:
        subprocess.run(['pip', 'install', dependency], cwd=directory)

    # Create requirements.txt
    subprocess.run(['pip', 'freeze', '>', 'requirements.txt'], shell=True, cwd=directory)

def display_pip_installs(pip_installs):
    """
    Display a table of pip installs.

    Args:
        pip_installs (list): List of pip installs.
    """
    # Create a new table
    table = Table(show_header=True, header_style="bold magenta")

    # Add columns to the table
    table.add_column("#", style="dim")
    table.add_column("Dependency")

    # Add rows to the table
    for i, dep in enumerate(pip_installs):
        table.add_row(str(i+1), dep)

    # Print the table
    console = Console()
    console.print(table)
