import os
import subprocess
from rich.console import Console
from rich.progress import Progress
from time import sleep
from automation.create_lab_repo.templates import test_file_template, file_template
from automation.create_lab_repo.user_prompts import user_prompts

console = Console()
progress = Progress()

def init_local_repo(directory, name):
    """
    Initialize a local repository with a specified name in the given directory.

    Args:
        directory (str): The directory path where the repository will be initialized.
        name (str): The name of the repository.

    Returns:
        str or bool: If the repository initialization is successful, returns the completed process confirmation string.
                     If the directory already exists and the user chooses not to initialize a repository, returns False.
    """
    # Create the new folder with the inputted name
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("Directory exists already use a different name")
        return user_prompts()
        
    # Run git init command in the newly made directory
    completed_process_confirm = subprocess.run(['git', 'init'], cwd=directory)
    
    # Create module folder
    module_name = name.replace("-", "_") if "-" in name else name
    module_folder = os.path.join(directory, module_name)
    os.makedirs(module_folder)
    
    # Create module script file
    module_script_file = os.path.join(module_folder, f"{module_name}.py")
    file_template(module_script_file, module_name)
    
    # Create tests folder
    tests_folder = os.path.join(directory, "tests")
    os.makedirs(tests_folder)
    
    # Create __init__.py file in tests folder
    init_py_file = os.path.join(tests_folder, "__init__.py")
    with open(init_py_file, 'a'):
        pass
    
    # Create test file for the module
    test_file = os.path.join(tests_folder, f"test_{module_name}.py")
    test_file_template(test_file, module_name)
    
    
    # Display message with spinner animation
    with console.status("[bold green]Repo initializing... ", spinner="moon"):
        sleep(3)        

    return str(completed_process_confirm)
