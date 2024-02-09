from automation.readings_scraper.scrape_elements import get_title, get_questions, get_readings, get_videos, get_bookmarks
from automation.readings_scraper.create_reading_file import create_reading_file
from rich.console import Console
from automation.readings_scraper.easter_eggs.class_ninetynine import class_ninetynine
from automation.readings_scraper.easter_eggs.class_301 import class_301
from automation.readings_scraper.easter_eggs.surprise_me import surprise_me
from automation.readings_scraper.easter_eggs.thanks_jb import thanks_jb

def readings_scraper():
    """
    Scrape reading assignment elements from the Code Fellows website and create a reading file.

    This function prompts the user to enter a class number (01-42) for which they want to create a reading assignment. 
    It then scrapes the title, questions, readings, videos, and bookmarks from the corresponding webpage 
    and creates a reading file with the obtained information.

    """
    console = Console()
    
    console.print("Which class number would you like to create a reading assignment for? Enter a number (01-42)", style="dodger_blue1")
    class_num = input("> ")
    if class_num == "99":
        return class_ninetynine()
    elif class_num == "301":
        return class_301()
    elif class_num == "42":
        console.print("The answer to life, the universe, and everything is 42", style="bold green")
    elif class_num.lower() == "thanks jb" or class_num.lower() == "thanksjb":
        return thanks_jb()
    elif class_num.lower() == "surprise me" or class_num.lower() == "surpriseme":
        return surprise_me()
    elif not class_num.isdigit():
        console.print("You must enter a class number (01-42).", style="bold red")
        readings_scraper()
    elif int(class_num) < 1 or int(class_num) > 42:
        console.print("You must enter a class number (01-42).", style="bold red")
        readings_scraper()
            
    url = f"https://codefellows.github.io/code-401-python-guide/curriculum/class-{class_num}/DISCUSSION"
    
    title = get_title(url)
    questions = get_questions(url)
    readings = get_readings(url)
    videos = get_videos(url)
    bookmarks = get_bookmarks(url)

    create_reading_file(title, class_num, questions, readings, videos, bookmarks)

# if __name__ == "__main__":
# readings_scraper()
