import pytest
from automation.create_local_repo import init_local_repo

@pytest.mark.skip
def test_local_repo_creation():
    actual = init_local_repo("../testing", "test02")
    expected = "CompletedProcess(args=['git', 'init'], returncode=0)"
    assert actual == expected

# @pytest.mark.skip
def test_no_directory():
    actual = init_local_repo()
    expected = "Directory and File name needed"
    assert actual == expected