from playwright.sync_api import sync_playwright
from scrape_elements import get_title

#TODO: find a way to pass username and password into the script
#TODO: ask JB for dummy account

class_num = "28"
url = "https://canvas.instructure.com/courses/8309911/discussion_topics/"

def create_reading_assignment(class_num):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)
        page.click(f"text=Read: Class {class_num}")
        print("clicked on Class")
        title = get_title(page)
        print("title: ", title)
        # questions = get_questions(url)
        # print("questions: ", questions)



# # with open("reading{class#}.md","w") as f:
# #     f.write("")


if __name__ == "__main__":
    create_reading_assignment(class_num)