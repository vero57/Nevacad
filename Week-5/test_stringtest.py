import pytest

@pytest.fixture
def email():
    return "vero@gmail.com"

def test_email(email):
    assert '@' in email




@pytest.fixture
def nama(request):
    nama = request.body.nama
    return nama

@pytest.mark.parametrize('nama', ['Vero'])
def test_nama(nama):
    assert nama == 'Vero'
