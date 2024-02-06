from automation.create_local_repo import init_local_repo
from automation.create_gitignore import create_gitignore
from automation.virtual_env import virtual_env_setup
from automation.create_github_repo import create_github_repo
import os
from rich.console import Console
from automation.create_readme import create_readme
import subprocess


def main():
    
    #Finds the users current directory parent directory
    current_directory=os.path.abspath(f'../{os.curdir}')

    # User prompts
    username = input("Enter your GitHub username: ")
    repo_name = input("Enter the repository name: ")


    # joins the directory and the repo name
    directory=os.path.join(f'{current_directory}/', f'{repo_name}')
    
    # Function calls
    init_local_repo(current_directory, repo_name)
    create_readme(directory)
    virtual_env_setup(directory)
    create_gitignore(directory)

    # Adds and Commits the local repo created
    subprocess.run(['git','add',"."], cwd=f"{directory}")
    subprocess.run(['git','commit','-m','"First Commit"'], cwd=f"{directory}")

    # links local repo and github repo
    create_github_repo(repo_name, username,directory)




if __name__ == "__main__":
    main()
