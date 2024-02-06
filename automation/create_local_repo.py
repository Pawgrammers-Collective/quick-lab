# As a user, I want to create a repo in my class folder with a name that I give it.

# Function takes in directory and name

# Dependencies: OS, shutil, subprocess, rich(probably)

# from rich.console import Console
import os
import shutil
import subprocess


def init_local_repo(directory, name):
#Make the new folder with the inputted name
    

    repo_path = f"{directory}/{name}"

# If directory doesn't already exists make
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
# Else if it exists, ask user if they still want to initialize
    else:
        print("Directory exists already")
        print("Would you like to still initialize a local repository in that directory? (y/n)")
        user_choice = input("> ")
        if user_choice.lower() == "y":
            subprocess.run(['git', 'init'], cwd=repo_path)
        else:
            return 

# run git init command in newly made directory
    subprocess.run(['git', 'init'], cwd=repo_path)



