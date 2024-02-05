from create_local_repo import init_local_repo
from create_gitignore import create_gitignore
from virtual_env import virtual_env_setup
from create_github_repo import create_github_repo
import os
from rich.console import Console
from create_readme import create_readme

def main():
    
    current_directory = os.path.abspath(os.curdir)
    repo_name = input("Enter the repository name: ")

    repo_name=init_local_repo(current_directory, repo_name)

    if repo_name is None:
        console=Console()
        console.print("Repository Name Needed", style="bold red" )
        return
    
    directory=os.path.join(current_directory, repo_name)



    create_readme()

    virtual_env_setup(directory)

    create_gitignore(directory)


    create_github_repo()

if __name__ == "__main__":
    main()
