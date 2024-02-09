from automation.create_lab_repo.create_lab_repo import create_lab_repo
from automation.readings_scraper.readings_scraper import readings_scraper
from automation.show_lab_guidelines.show_lab_guidelines import show_lab_guidelines
from rich.console import Console
from rich.prompt import Prompt


def main():
    """
    Main function to present options to the user and perform actions based on their choice.
    """
    console = Console()
    while True:
        console.print("\n1. [bold green]Create Lab Repo[/bold green] \U0001F4BE\n2. [bold blue]Create Reading Assignment[/bold blue] \U0001F4DA\n3. [yellow]Show Lab Submission Instructions[/yellow] \U0001F4A1\n4. [bold red]Exit[/bold red] \U0001F6AA")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4'], default='4')

        if choice == '1':
            create_lab_repo()
        elif choice == '2':
            readings_scraper()
        elif choice == '3':
            show_lab_guidelines()
        else:
            break


if __name__ == "__main__":
    main()
