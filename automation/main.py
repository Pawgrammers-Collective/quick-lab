from automation.create_local_repo import init_local_repo
from automation.create_gitignore import create_gitignore
from automation.create_github_repo import create_github_repo
from automation.user_prompts import user_prompts
from automation.create_pip_install import create_pip_install
from automation.create_readme import create_readme
from automation.readings_scraper.readings_scraper import create_reading_assignment
from automation.check_gh_stuff import check_gh_user, check_gh_repo_exists
from rich.console import Console
from rich.prompt import Prompt


def main():
    console = Console()
    while True:
        console.print("\n1. [bold green]Create Lab Repo[/bold green]\n2. [bold blue]Create Reading Assignment[/bold blue]\n3. [bold red]Exit[/bold red]")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3'], default='3')

        if choice == '1':
            create_lab_repo()
        elif choice == '2':
            class_num = Prompt.ask("Which class number would you like to create a reading assignment for?")
            create_reading_assignment(class_num)
        else:
            break
    

def create_lab_repo():
    # Function calls
    directory, username, repo_name, pip_installs = user_prompts()
    init_local_repo(directory, repo_name)
    create_readme(directory)
    create_pip_install(pip_installs, directory)
    create_gitignore(directory)
    create_github_repo(repo_name, username, directory)


if __name__ == "__main__":
    main()