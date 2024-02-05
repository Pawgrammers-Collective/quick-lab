# TODO: create empty github repo; do not initialize with README.md, license, or gitignore
# TODO: copy "Quick Setup" url
from playwright.sync_api import sync_playwright
import subprocess
# from page_parser import parse
# import os
# import sys
# import requests


username = "JohnnyBackus"
print("I'm alive")
repo_name = "ql-test5"
# directory = f"Users/johnnymac/projects/code-401/{repo_name}"
subprocess.run(["gh", "repo", "create", repo_name, "--public", f"--source=.", "--remote=upstream"])

def create_github_repo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # context = browser.new_context()
        page = browser.new_page()
        page.goto(f"https://github.com/{username}/{repo_name}")
#         # page.click("text=Create new")#button id="global-create-menu-button"
#         # page.click("text=New repository")#li data-analytics-event="...,"label":"new_repository"
#         # page.goto("https://github.com/new")
#         # page.fill("input[name='repository[name]']", {repo_name})
#         # page.click("text=Create repository")
        new_repo_url = page.eval_on_selector("#empty-setup-push-repo-echo > span:nth-child(1) > span")
#         print(new_repo_url)
        subprocess.run(["git", "remote", "add", "origin", new_repo_url])
        subprocess.run(["git", "branch", "-M", "main"])
        subprocess.run(["git", "push", "-u", "origin", "main"])


# subprocess.run(["git", "remote", "add", "origin", new_repo_url])
# subprocess.run(["git", "branch", "-M", "main"])
# subprocess.run(["git", "push", "-u", "origin", "main"])

create_github_repo()