import os
from tkinter import filedialog
import tkinter
from automation.create_lab_repo.create_pip_install import create_pip_install, display_pip_installs
from automation.create_lab_repo.check_gh_stuff import check_gh_repo_exists, check_gh_user
from rich.console import Console

def user_prompts():
    """
    Function to prompt the user for necessary information to create a GitHub repository and optionally install pip dependencies.

    Returns:
        tuple: A tuple containing directory path, GitHub username, repository name, and a list of pip dependencies.
    """

    # List for the user's pip installs
    pip_installs = []
    pip_questions = True
    login_question = True

    current_directory = ""

    # Checks if the user is logged in
    while login_question:
        console = Console()
        console.print("\nFor this to work properly you need to be logged into GitHub on your browser.", style="bold green")
        question = input('Are you logged in? (y/n): ')

        if question == "y":
            login_question = False

    # User prompts
    console = Console()
    user_exists = False
    while user_exists is False:
        console.print("\nEnter your GitHub username:", style="orange1")
        username = input("> ")
        user_exists = check_gh_user(username)
        if user_exists is False:
            console.print("This username does not exist!", style="bold red")
    
    repo_exists = True
    while repo_exists is True:
        console.print("\nEnter the repository name:", style="magenta1")
        repo_name = input("> ")
        repo_exists = check_gh_repo_exists(username, repo_name)
        if repo_exists is True:
            console.print("This remote repository is already made!", style="bold red")

    # Prompt for choosing the directory
    console.print(f"\nThis program will create a {repo_name} folder for you at the same level as this program, if one doesn't already exist. Would you like to choose a different location for your lab repo instead? (y/n):", style="green3")
    choose_directory = input("> ")

    if choose_directory.lower() == "y":
        root = tkinter.Tk()

        current_directory = filedialog.askdirectory(title="Choose directory for repository",parent=root)
        root.withdraw()
        directory = os.path.join(f'{current_directory}/', f'{repo_name}')

    else:
        # Finds the user's current directory parent's directory
        current_directory = os.path.abspath(f'../{os.curdir}')
        # Joins the directory and the repo name
        directory = os.path.join(f'{current_directory}/', f'{repo_name}')

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

    return directory, username, repo_name, pip_installs
