from automation.create_lab_repo.create_lab_repo import create_lab_repo
from automation.readings_scraper.readings_scraper import readings_scraper
from rich.console import Console
from rich.prompt import Prompt


def main():
    """
    Main function to present options to the user and perform actions based on their choice.
    """
    console = Console()
    while True:
        console.print("\n1. [bold green]Create Lab Repo[/bold green]\n2. [bold blue]Create Reading Assignment[/bold blue]\n3. [bold red]Exit[/bold red]")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3'], default='3')

        if choice == '1':
            create_lab_repo()
        elif choice == '2':
            readings_scraper()
        else:
            break


if __name__ == "__main__":
    main()
