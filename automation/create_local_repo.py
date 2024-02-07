# As a user, I want to create a repo in my class folder with a name that I give it.

# Function takes in directory and name

# Dependencies: OS, shutil, subprocess, rich(probably)

# from rich.console import Console
import os
import shutil
import subprocess


def init_local_repo(directory, name):
#Make the new folder with the inputted name
    

    # repo_path = f"{directory}/{name}"
    # print("repo path is:", repo_path)

# If directory doesn't already exists make
    print('the directory is:',directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
# Else if it exists, ask user if they still want to initialize
    else:
        print("Directory exists already")
        print("Would you like to still initialize a local repository in that directory? (y/n)")
        user_choice = input("> ")
        if user_choice.lower() == "n":
            return False
        
# run git init command in newly made directory
    completed_process_confirm = subprocess.run(['git', 'init'], cwd=directory)



 # Create module folder
    if "-" in name:
        module_name = name.replace("-", "_")
    else:
        module_name = name    
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

    return str(completed_process_confirm)