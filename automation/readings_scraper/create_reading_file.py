import os
from tkinter import filedialog
from rich.console import Console
from automation.readings_scraper.choose_file_name import choose_file_name
from automation.readings_scraper.choose_directory import choose_directory
# from automation.main import main

console = Console()

def create_reading_file(title, class_num, questions, readings, videos, bookmarks):

    file_name = choose_file_name(class_num)
    file_path = choose_directory(file_name)
    if not file_path:
        return
    create_template (title, questions, readings, videos, bookmarks, file_path)


def create_template(title, questions, readings, videos, bookmarks, file_path):

    # Define the template
    template = f"""
# {title}

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
        file.write(f"# {template}")
        console.print('File created successfully!', style = "bold spring_green3")
        