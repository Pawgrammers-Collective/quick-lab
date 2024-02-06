# test_create_gitignore.py

import unittest
import os
import shutil
from automation.create_gitignore import create_gitignore

class TestCreateGitignore(unittest.TestCase):

    def test_create_gitignore(self):
        # Set up a temporary directory for testing
        test_directory = 'test_directory'
        os.makedirs(test_directory)

        try:
            # Call the create_gitignore function
            create_gitignore(test_directory)

            # Check if the .gitignore file is created
            self.assertTrue(os.path.exists(os.path.join(test_directory, '.gitignore')))

            # Check if the contents of the .gitignore file are as expected
            with open(os.path.join(test_directory, '.gitignore'), 'r') as gitignore_file:
                gitignore_contents = gitignore_file.read()
                self.assertIn('.venv', gitignore_contents)

        finally:
            # Clean up: Remove the temporary directory
            shutil.rmtree(test_directory)

if __name__ == '__main__':
    unittest.main()
