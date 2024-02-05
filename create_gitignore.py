"""
Function creates .gitignore after script initialization.  Adds .venv(for starters) to .gitignore

params:
- None

Returns:
- None but .gitignore will be created
"""

import os 
import shutil
import platform


def create_gitignore(directory='.'):
  
#   Opens the gitignore contents in this package, stores it as a template to 
  with open('./.gitignore', 'r') as gitignore_template:
    gitignore_contents = gitignore_template.read()

# Creates a gitignore in the user's desired directory with the gitignore contents
  with open(f'{directory}/.gitignore', 'w') as gitignore:
    gitignore.write(gitignore_contents)