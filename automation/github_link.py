import subprocess

def repo_link(directory, github_repo_link):

    if github_repo_link:

        subprocess.run([f"git remote add origin {github_repo_link}"], cwd=f"{directory}")

        subprocess.run(["git branch -M main"], cwd=f"{directory}")

        subprocess.run(["git push -u origin main"], cwd=f"{directory}")

        