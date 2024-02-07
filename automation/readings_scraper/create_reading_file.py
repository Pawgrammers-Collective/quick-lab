import os
from rich.console import Console
# from automation.main import main

console = Console()

def create_reading_file(title, class_num, questions, readings, videos, bookmarks):
   
    user_directory = os.path.abspath(f'../{os.curdir}')
    file_name = f"reading{class_num}.md"
    folder_path = os.path.join(f'{user_directory}/reading_assignments')
    file_path = os.path.join(f'{folder_path}/{file_name}')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    if os.path.exists(file_path):
        console.print("\nThis file already exists.", style="bold red")
        user_input= input("Would you like to overwrite it? (y/n): ")
        
        if user_input == "y":
            console.print("File will be overwritten.", style="bold yellow")
        
        elif user_input == "n":
            console.print("File not created.", style="bold green")
            create_reading_file(title, class_num, questions, readings, videos, bookmarks)

        else:
            console.print("Response not recognized. Returning to main menu.", style="bold red")
            create_reading_file(title, class_num, questions, readings, videos, bookmarks)

    create_template (title, questions, readings, videos, bookmarks, file_path)


def create_template(title, questions, readings, videos, bookmarks, file_path):

    # Define the template
    template = f"""# {title}

Description of the assignment

## Reading\n
{readings.strip()}

## Videos\n
{videos.strip()}

## Bookmark and Review\n
{bookmarks.strip()}

## Reading Questions\n
{questions.strip()}

## Things I want to know more about

>*Answer*
"""

    with open(file_path, "w") as file:
        file.write(f"{template}")
        console.print('File created successfully!', style = "bold spring_green3")
        

