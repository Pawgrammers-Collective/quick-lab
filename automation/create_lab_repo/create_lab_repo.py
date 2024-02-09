from automation.create_lab_repo.init_local_repo import init_local_repo
from automation.create_lab_repo.create_gitignore import create_gitignore
from automation.create_lab_repo.create_github_repo import create_github_repo
from automation.create_lab_repo.user_prompts import user_prompts
from automation.create_lab_repo.create_pip_install import create_pip_install
from automation.create_lab_repo.create_readme import create_readme


def create_lab_repo():
    """
    Function to create a lab repository with necessary files and configurations.
    """
    # Function calls
    directory, username, repo_name, pip_installs = user_prompts()
    init_local_repo(directory, repo_name)
    create_readme(directory)
    create_pip_install(pip_installs, directory)
    create_gitignore(directory)
    create_github_repo(repo_name, username, directory)
