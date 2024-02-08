import requests

def check_gh_user(username):
    """
    Check if a GitHub user exists.

    Args:
        username (str): The GitHub username to check.

    Returns:
        bool: True if the user exists, False if not.
        None: If an error occurs during the request.
    """
    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return None


def check_gh_repo_exists(username, repo):
    """
    Check if a GitHub repository exists.

    Args:
        username (str): The GitHub username.
        repo (str): The repository name.

    Returns:
        bool: True if the repository exists, False if not.
        None: If an error occurs during the request.
    """
    response = requests.get(f"https://api.github.com/repos/{username}/{repo}")

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return None
