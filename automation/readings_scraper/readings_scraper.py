from tkinter import filedialog
import os
from automation.readings_scraper.scrape_elements import get_title, get_questions, get_readings, get_videos, get_bookmarks
from automation.readings_scraper.create_reading_file import create_reading_file
from rich.console import Console


def readings_scraper(class_num=33):
    console = Console()
    
    console.print("Which class number would you like to create a reading assignment for?", style = "dodger_blue1")
    class_num = input("> ")
    
    url = f"https://codefellows.github.io/code-401-python-guide/curriculum/class-{class_num}/DISCUSSION"
    
    title = get_title(url)
    questions = get_questions(url)
    readings = get_readings(url)
    videos = get_videos(url)
    bookmarks = get_bookmarks(url)

    create_reading_file (title, class_num, questions, readings, videos, bookmarks)

    # return title, questions, readings, videos, bookmarks

# if __name__ == "__main__":
# create_reading_assignment(34)