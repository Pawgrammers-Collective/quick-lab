import os
import subprocess
from rich.console import Console
from rich.progress import Progress
from time import sleep

console = Console()
progress=Progress()

def init_local_repo(directory, name):
    # Make the new folder with the inputted name
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("Directory exists already")
        print("Would you like to still initialize a local repository in that directory? (y/n)")
        user_choice = input("> ")
        if user_choice.lower() == "n":
            return False
        
    # Run git init command in the newly made directory
    completed_process_confirm = subprocess.run(['git', 'init'], cwd=directory)
    
    # Create module folder
    module_name = name.replace("-", "_") if "-" in name else name
    module_folder = os.path.join(directory, module_name)
    os.makedirs(module_folder)
    
    # Create module script file
    module_script_file = os.path.join(module_folder, f"{module_name}.py")
    with open(module_script_file, 'w') as module_file_content:
        module_file_content.write(f'def {module_name}():\n pass\n')
    
    # Create tests folder
    tests_folder = os.path.join(directory, "tests")
    os.makedirs(tests_folder)
    
    # Create __init__.py file in tests folder
    init_py_file = os.path.join(tests_folder, "__init__.py")
    with open(init_py_file, 'a'):
        pass
    
    # Create test file for the module
    test_file = os.path.join(tests_folder, f"test_{module_name}.py")
    with open(test_file, 'w') as test_file_content:
        test_file_content.write(f'import pytest\n')
        test_file_content.write(f'from {module_name}.{module_name} import {module_name} ')
    
    
   # Display message with spinner animation
    with console.status("[bold green]Repo initializing... ", spinner="moon"):
        sleep(3)        

    return str(completed_process_confirm)
