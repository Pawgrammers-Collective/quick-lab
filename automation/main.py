
from create_local_repo import init_local_repo
from create_gitignore import create_gitignore
from virtual_env import virtual_env_setup
from create_github_repo import create_github_repo
import os
from rich.console import Console

def main():
    # Specify your directory and repo name
    current_directory = os.path.abspath(os.curdir)
    repo_name = input("Enter the repository name: ")
    # Task 1: Create a local repo

    repo_name=init_local_repo(current_directory, repo_name)

    if repo_name is None:
        console=Console()
        console.print("Repository Name Needed", style="bold red" )
        return
    
    directory=os.path.join(current_directory, repo_name)




    # Task 2: Create .gitignore
    create_gitignore(directory)

    # Task 3: Set up virtual environment
    virtual_env_setup(directory)

    # Task 4: Create GitHub repo and push local repo
    create_github_repo()

if __name__ == "__main__":
    main()
