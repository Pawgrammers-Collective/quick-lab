
def test_file_template(test_file, module_name):


    test_template = f"""
import pytest
from {module_name}.{module_name} import {module_name} 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = {module_name}()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = {module_name}(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

"""


    with open(test_file, 'w') as test_file_content:
        test_file_content.write(test_template)


def file_template(module_script_file, module_name):


    test_template = f"""
# Import stuff

# From stuff import things

    

def {module_name}(demo_fixture=""):

    if demo_fixture:
        return demo_fixture
 
    return "Starter test"

"""


    with open(module_script_file, 'w') as module_file_content:
        module_file_content.write(test_template)
    
