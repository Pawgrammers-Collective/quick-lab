import os


def user_prompts():

    # list for the users pip installs
    pip_installs = []
    pip_questions = True
    login_question = True


    # Checks if the user is logged in
    while login_question:
        question = input('For this to work properly you need to be logged into github on your browser.\nAre you logged in?\n(y/n):')

        if question == "y":
            login_question = False


    # User prompts
    username = input("Enter your GitHub username: ")
    repo_name = input("Enter the repository name: ")
    while pip_questions:

        pip = input("Enter a dependency that you want to install: ")
        pip_installs.append(pip)

        exit_question = str(input("Do you want to add more dependencies(y/n): "))

        if exit_question == "n":
            pip_questions = False


    #Finds the users current directory parents directory
    current_directory=os.path.abspath(f'../{os.curdir}')


    # joins the directory and the repo name
    directory=os.path.join(f'{current_directory}/', f'{repo_name}')


    return current_directory, directory, username, repo_name, pip_installs