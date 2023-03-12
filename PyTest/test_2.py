import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_stringProgram():
    msg = 'Hello'
    assert msg == 'Hi', 'Test failed because strings did not match'


def test_additionProgram():
    a = 2
    b = 2
    assert a + 2 == 4, 'Int did not match'
