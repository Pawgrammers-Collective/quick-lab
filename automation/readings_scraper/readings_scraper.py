from scrape_elements import get_title, get_questions, get_readings, get_videos, get_bookmarks
from create_reading_file import create_reading_file


def create_reading_assignment(class_num=33):
    url = f"https://codefellows.github.io/code-401-python-guide/curriculum/class-{class_num}/DISCUSSION"
    title = get_title(url)
    # print("title: ", title)
    questions = get_questions(url)
    # print("questions: ", questions)
    readings = get_readings(url)
    # print("readings: ", readings)
    videos = get_videos(url)
    # print("videos: ", videos)
    bookmarks = get_bookmarks(url)
    # print("bookmarks: ", bookmarks)

    create_reading_file (title, class_num, questions, readings, videos, bookmarks)

    # return title, questions, readings, videos, bookmarks

if __name__ == "__main__":
    create_reading_assignment(33)