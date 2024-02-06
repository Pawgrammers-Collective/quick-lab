# test_create_gitignore.py

import pytest
import os
import shutil
from automation.create_gitignore import create_gitignore



# @pytest.mark.skip
def test_create_gitignore():
    actual = create_gitignore()
    expected = True
    assert actual == expected
