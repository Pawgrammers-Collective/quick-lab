from bs4 import BeautifulSoup
import requests


def get_title(url): #shared function to find assignment title
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    try:
        title_soup = soup.find("h1")
        title = title_soup.text
    except:
        title = []
    return title #returns a list


def get_questions(url): #shared function to find assignment questions
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    try:
        questions_soup = soup.find("h2", id="reading-questions").find_next_sibling("ol").findAll("li")#finds all <li> tags that are the children of the ol tag that is the sibling of the h2 tag with the id "reading-questions"
        questions = [q.text for q in questions_soup]
    except:
        questions = []
    return questions #returns a list


def get_readings(url): #shared function to find assignment sources
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    try:
        readings_soup = soup.find("h2", id="reading").find_next_siblings("p")#finds all <p> tags that are the siblings of h2 tag with the id "reading"
        # print("readings_soup: ", readings_soup)
        readings_text = [s.text for s in readings_soup]
        readings_url = [s.find("a")["href"] for s in readings_soup if s.find("a")]#finds all <a> tags that are the children of the <p> tags
        # print("sources: ", readings_text, readings_url)
    except:
        readings_text = []
        readings_url = []      
    return readings_text, readings_url #returns two lists


def get_videos(url): #shared function to find assignment videos
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    try:
        videos_soup = soup.find("h2", id="videos").find_next_siblings("p")#finds all <p> tags that are the siblings of h2 tag with the id "videos"
        # print("videos_soup: ", videos_soup)
        videos_text = [v.text for v in videos_soup]
        videos_url = [v.find("a")["href"] for v in videos_soup if v.find("a")]#finds all <a> tags that are the children of the <p> tags
        print("videos: ", videos_text, videos_url)
    except:
        videos_text = []
        videos_url = [] 
    return videos_text, videos_url #returns two lists


def get_bookmarks(url): #shared function to find assignment videos
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    try:
        bookmarks_soup = soup.find("h2", id="bookmark-and-reivew").find_next_siblings("p")#finds all <p> tags that are the siblings of h2 tag with the id "bookmark-and-review"
        bookmarks_text = [b.text for b in bookmarks_soup]
        bookmarks_url = [b.find("a")["href"] for b in bookmarks_soup if b.find("a")]#finds all <a> tags that are the children of the <p> tags
        print("videos: ", bookmarks_text, bookmarks_url)
    except:
        bookmarks_text = []
        bookamrks_url = []  
    return bookmarks_text, bookamrks_url #returns two lists

