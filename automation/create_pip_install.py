import subprocess

def create_pip_install(dependencies, directory):
    """
    Install pip dependencies and create requirements.txt.

    Args:
        dependencies (list): List of pip dependencies to install.
    """
    # Install dependencies
    for dependency in dependencies:
        subprocess.run(['pip', 'install', dependency], cwd=directory)

    # Create requirements.txt
    subprocess.run(['pip', 'freeze', '>', 'requirements.txt'], shell=True, cwd=directory)
