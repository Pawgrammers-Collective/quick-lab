from bs4 import BeautifulSoup
import requests


def get_title(url): #shared function to find assignment title
    response = requests.get(url)
    # print("response: ", response)
    text = response.text
    # print("text: ", text)
    soup = BeautifulSoup(text, "html.parser")
    # print("soup: ", soup)
    title_soup = soup.find("h1")
    # print("title_soup: ", title_soup)
    title = title_soup.text
    # print("title: ", title)
    return title #returns a list


def get_questions(url): #shared function to find assignment questions
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    questions_soup = soup.find("h2", id="reading-questions").find_next_sibling("ol").findAll("li")#finds all <li> tags that are the children of the 1st child section of div with the class "wrapper"
    # print("questions_soup: ", questions_soup)
    questions = [q.text for q in questions_soup]
    # print("questions: ", questions)
    return questions #returns a list


