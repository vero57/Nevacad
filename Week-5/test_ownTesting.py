import pytest

@pytest.fixture
def username():
    return 'Rusdi grobogan'

def test_username(username):
    assert username == 'Rusdi grobogan'


@pytest.fixture
def XISIJA1():
    nama == request.body.XISIJA1
    return XISIJA1

@pytest.mark.parametrize('XISIJA1', ['Arya Zaka'])
def test_XISIJA1(XISIJA1):
    assert XISIJA1 =='Arya Zaka'