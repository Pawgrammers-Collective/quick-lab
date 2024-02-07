# from playwright.sync_api import sync_playwright
from scrape_elements import get_title, get_questions
import os
# from dotenv import load_dotenv
# load_dotenv()

#TODO: find a way to pass username and password into the script

# username = "john.p.backus@gmail.com"
# password = "SEPtRh8^uY%DL#"
# username = os.getenv('CANVAS_USERNAME')
# password = os.getenv('CANVAS_PASSWORD')

class_num = "28"
# url = "https://canvas.instructure.com/courses/8309911/discussion_topics/"
url = f"https://codefellows.github.io/code-401-python-guide/curriculum/class-{class_num}/DISCUSSION"


def create_reading_assignment():
    title = get_title(url)
    print("title: ", title)
    questions = get_questions(url)
    print("questions: ", questions)
   
    folder_path = "../reading_assignments"
    file_name = f"reading{class_num}.md"
    file_path = os.path.join(folder_path,"/",file_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the file
    with open(file_path, "w") as file:
        file.write(f"# {title}\n\n {questions}")


# def create_reading_assignment(class_num):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(url)
#         page.fill('input[name="pseudonym_session[unique_id]"]', username)
#         page.fill('input[name="pseudonym_session[password]"]', password)
#         page.click('input[type="submit"]')
#         page.click(f"text=Read: Class {class_num}")
#         print("clicked on Class")
#         title = get_title(page)
#         print("title: ", title)
        # questions = get_questions(url)
        # print("questions: ", questions)






if __name__ == "__main__":
    create_reading_assignment()