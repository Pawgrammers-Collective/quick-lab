import subprocess
from rich.console import Console

def create_github_repo(repo_name, username, directory):
    """
    Create a GitHub repository and link it with the local repository.

    Args:
        repo_name (str): The name of the GitHub repository.
        username (str): The GitHub username of the user.
        directory (str): The directory path of the local repository.

    """
    # Adds and Commits the local repo created
    subprocess.run(['git','add',"."], cwd=f"{directory}")
    subprocess.run(['git','commit','-m','"First Commit"'], cwd=f"{directory}")

    # Uses CLI to create a GitHub repo
    subprocess.run(["gh", "repo", "create", repo_name, "--public", f"--source=.", "--remote=upstream"], cwd=f"{directory}")

    # Links to the repos, branches to main, and pushes.
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{username}/{repo_name}.git"], cwd=f"{directory}")
    subprocess.run(["git", "branch", "-M", "main"], cwd=f"{directory}")
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=f"{directory}")

    # Print success message
    console = Console()
    console.print("\nSuccessfully created and linked the local repository to the remote repository on GitHub.", style="bold green")
    console.print("Don't forget to activate the virtual environment in your new repo!\n", style="bold green")
