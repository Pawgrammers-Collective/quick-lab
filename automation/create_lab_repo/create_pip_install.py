import subprocess
from rich.table import Table
from rich.console import Console
import platform
import os

def create_pip_install(dependencies, directory):
    """
    Install pip dependencies and create requirements.txt file.

    Args:
        dependencies (list): List of pip dependencies to install.
        directory (str): Directory to install dependencies and create requirements.txt.
        
    Returns:
        bool: True if the virtual environment (.venv) is successfully created, False otherwise.
    """
    # Check the operating system
    pc_type = platform.system()

    # Create .venv directory in the specified directory
    subprocess.run(["python3", "-m", "venv", ".venv"], cwd=directory)

    if pc_type == "Darwin":  # For macOS

        # Install dependencies
        for dependency in dependencies:
            subprocess.run([f'{directory}/.venv/bin/pip', 'install', dependency], cwd=directory, text=True)
        
        # Freeze dependencies and write to requirements.txt
        result = subprocess.run([f'{directory}/.venv/bin/pip', 'freeze'], cwd=directory, capture_output=True, text=True)
        with open(f'{directory}/requirements.txt', 'w') as requirements_file:
            requirements_file.write(result.stdout)
        
    elif pc_type == "Windows":  # For Windows

        # Install dependencies
        for dependency in dependencies:
            subprocess.run([f'{directory}/.venv/Scripts/pip', 'install', dependency], cwd=directory, text=True)

        # Freeze dependencies and write to requirements.txt
        result = subprocess.run([f'{directory}/.venv/Scripts/pip', 'freeze'], cwd=directory, capture_output=True, text=True)
        with open(f'{directory}/requirements.txt', 'w') as requirements_file:
            requirements_file.write(result.stdout)

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
