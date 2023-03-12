# Any pytest file should start with name test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


def test_greet():
    print('Good Morning')


@pytest.mark.xfail
def test_greetCredit():
    print('Good Morning')


def test_crossBrowser(crossBrowser):
    print(crossBrowser)