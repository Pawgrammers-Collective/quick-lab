from automation.create_local_repo import init_local_repo
from automation.create_gitignore import create_gitignore
from automation.virtual_env import virtual_env_setup
from automation.create_github_repo import create_github_repo
from automation.user_prompts import user_prompts
from automation.create_pip_install import create_pip_install
from automation.create_readme import create_readme




def main():
    
    # Function calls
    current_directory, directory, username, repo_name, pip_installs = user_prompts()
    init_local_repo(current_directory, repo_name)
    create_readme(directory)
    virtual_env_setup(directory)
    create_pip_install(pip_installs, directory)
    create_gitignore(directory)
    create_github_repo(repo_name, username, directory)


if __name__ == "__main__":
    main()
