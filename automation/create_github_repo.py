import subprocess
from rich.console import Console

def create_github_repo(repo_name, username, directory):
    # Adds and Commits the local repo created
    subprocess.run(['git','add',"."], cwd=f"{directory}")
    subprocess.run(['git','commit','-m','"First Commit"'], cwd=f"{directory}")

    # Uses CLI to create a github repo
    subprocess.run(["gh", "repo", "create", repo_name, "--public", f"--source=.", "--remote=upstream"], cwd=f"{directory}")

    # Links to the repos, branches to main, and pushes.
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{username}/{repo_name}.git"], cwd=f"{directory}")
    subprocess.run(["git", "branch", "-M", "main"], cwd=f"{directory}")
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=f"{directory}")

    # Print success message
    console = Console()
    console.print("\nSuccessfully created and linked the local repository to the remote repository on GitHub.", style="bold green")
    console.print("Don't forget to activate the virtual environment in your new repo!\n", style="bold green")

