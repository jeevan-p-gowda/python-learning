import pytest


# Fixtures are used to run prior to actual tests and after tests
# having fixture in conftest.py makes available to all .py file methods
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


# in case if we are using return statement in place of yield, the print will be unreachable
# we cannot use yield and return both
# we can use yield to print the lis, or let it go
@pytest.fixture()
def exampleYield():
    print("First")
    lis = [1, 2, 3]
    yield lis
    print("End")
