from automation.create_local_repo import init_local_repo
from automation.create_gitignore import create_gitignore
from automation.virtual_env import virtual_env_setup
from automation.create_github_repo import create_github_repo
import os
from rich.console import Console
from automation.create_readme import create_readme
import subprocess

def main():
    
    os.path.abspath(os.curdir)
    current_directory=os.chdir('..')
    username = input("Enter your GitHub username: ")
    repo_name = input("Enter the repository name: ")



    directory=os.path.join(f'{current_directory}/', f'{repo_name}')

    init_local_repo(current_directory, repo_name)

    create_readme(directory)

    virtual_env_setup(directory)

    create_gitignore(directory)

    subprocess.run(['git','add',"."], cwd=f"{directory}")

    subprocess.run(['git','commit','-m','"First Commit"'], cwd=f"{directory}")

    create_github_repo(repo_name, username,directory)




if __name__ == "__main__":
    main()
