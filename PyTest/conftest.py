import pytest


# Fixtures are used to run prior to actual tests
# having fixture in conftest.py makes available to all .py file methods
# @pytest.fixture()
@pytest.fixture(scope="class")
def setup():
    print('I will be executing first')
    yield  # runs after test
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Jeevan", "Rajeev", "Chandra"]


@pytest.fixture(params=[("chrome", "Jeevan", "Gowda"), "Firefox", "IE"])
def crossBrowser(request):
    return request.param
