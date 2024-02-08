import pytest
import os
import shutil
from unittest.mock import patch
from automation.create_lab_repo.create_local_repo import init_local_repo
from automation.create_lab_repo.create_gitignore import create_gitignore
from automation.create_lab_repo.create_readme import create_readme
from automation.create_lab_repo.check_gh_stuff import check_gh_user, check_gh_repo_exists

# @pytest.mark.skip
def test_local_repo_creation(test_directory):

    with patch('builtins.input', return_value='y'):
        actual = init_local_repo(test_directory, "test_pytest")
    expected = "CompletedProcess(args=['git', 'init'], returncode=0)"
    assert actual == expected

# @pytest.mark.skip
def test_no_to_previously_made_directory(test_directory):
  with patch('builtins.input', return_value= 'n'):
        assert not init_local_repo(test_directory, "test_pytest")

# @pytest.mark.skip
def test_create_gitignore(test_directory):
    actual = create_gitignore(test_directory)
    expected = True
    assert actual == expected

# @pytest.mark.skip
def test_create_readme(test_directory):
    actual = create_readme(test_directory)
    expected = True
    assert actual == expected

# @pytest.mark.skip
def test_check_gh_user_true():
    actual = check_gh_user("brendanhuddleston18")
    expected = True
    assert actual == expected

# @pytest.mark.skip
def test_check_gh_user_false():
    actual = check_gh_user("xxbob-saget-was-a-gov-spy20")
    expected = False
    assert actual == expected

# @pytest.mark.skip
def test_gh_repo_exists_true():
    actual = check_gh_repo_exists("brendanhuddleston18", "ten-thousand")
    expected = True
    assert actual == expected

# @pytest.mark.skip
def test_gh_repo_exists_false():
    actual = check_gh_repo_exists("xxbob-saget-was-a-gov-spy20", "ten-thousand")
    expected = False
    assert actual == expected


@pytest.fixture
def test_directory():
    path = "../pytest-testing"

    os.makedirs(path, exist_ok=True)

    yield path

    shutil.rmtree(path, ignore_errors=True)