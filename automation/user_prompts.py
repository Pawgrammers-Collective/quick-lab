import os
from create_pip_install import display_pip_installs
from rich.console import Console

def user_prompts():
    # List for the user's pip installs
    pip_installs = []
    pip_questions = True
    login_question = True

    # Checks if the user is logged in
    while login_question:
        console = Console()
        console.print("\nFor this to work properly you need to be logged into GitHub on your browser.", style="bold green")
        question = input('Are you logged in? (y/n): ')

        if question == "y":
            login_question = False

    # User prompts
    console = Console()
    console.print("\nEnter your GitHub username:", style="orange1")
    username = input("> ")
    
    console.print("\nEnter the repository name:", style="magenta1")
    repo_name = input("> ")

    # Prompt for installing pip dependencies
    console.print("\nDo you want to install any pip dependencies before proceeding? (y/n):", style="green3")
    install_pip_dependencies = input("> ")

    if install_pip_dependencies.lower() == "y":
        while pip_questions:
            console.print("\nEnter a dependency that you want to install:", style="hot_pink")
            pip = input("> ")

            # Check if the dependency already exists in the list
            while pip in pip_installs:
                console.print("\nDependency already exists. Please enter a different dependency:", style="bold red")
                pip = input("> ")

            pip_installs.append(pip)

            # Display table of pip installs
            display_pip_installs(pip_installs)

            valid_input = False
            while not valid_input:
                console.print("\nDo you want to add more dependencies? (y/n):", style="green3")
                exit_question = input("> ")

                if exit_question == "y" or exit_question == "n":
                    valid_input = True
                else:
                    console.print("\nInvalid input. Please enter 'y' or 'n'.", style="bold red")

            if exit_question == "n":
                pip_questions = False

    # Finds the user's current directory parent's directory
    current_directory = os.path.abspath(f'../{os.curdir}')

    # Joins the directory and the repo name
    directory = os.path.join(f'{current_directory}/', f'{repo_name}')

    return current_directory, directory, username, repo_name, pip_installs
