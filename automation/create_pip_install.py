import subprocess

def create_pip_install(dependencies):
    """
    Install pip dependencies and create requirements.txt.

    Args:
        dependencies (list): List of pip dependencies to install.
    """
    # Install dependencies
    for dependency in dependencies:
        subprocess.run(['pip', 'install'] + dependency)

    # Create requirements.txt
    subprocess.run(['pip', 'freeze', '>', 'requirements.txt'], shell=True)
