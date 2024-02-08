import os
from tkinter import filedialog
from rich.console import Console
from automation.readings_scraper.choose_file_name import choose_file_name
from automation.readings_scraper.choose_directory import choose_directory

console = Console()

def create_reading_file(title, class_num, questions, readings, videos, bookmarks):
    """
    Create a reading file with the provided elements.

    Args:
        title (str): The title of the reading assignment.
        class_num (str): The class number associated with the reading assignment.
        questions (str): Questions related to the reading assignment.
        readings (str): Readings for the assignment.
        videos (str): Videos related to the assignment.
        bookmarks (str): Bookmark and review links.

    """
    file_name = choose_file_name(class_num)
    file_path = choose_directory(file_name)
    if not file_path:
        return
    create_template(title, questions, readings, videos, bookmarks, file_path)


def create_template(title, questions, readings, videos, bookmarks, file_path):
    """
    Create a template for the reading file.

    Args:
        title (str): The title of the reading assignment.
        questions (str): Questions related to the reading assignment.
        readings (str): Readings for the assignment.
        videos (str): Videos related to the assignment.
        bookmarks (str): Bookmark and review links.
        file_path (str): The path where the reading file will be saved.

    """
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
        console.print('File created successfully!', style="bold spring_green3")
