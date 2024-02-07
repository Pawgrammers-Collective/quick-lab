import requests

def check_gh_user(username):

    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return None


def check_gh_repo_exists(username, repo):
    
    response = requests.get(f"https://api.github.com/repos/{username}/{repo}")

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return None