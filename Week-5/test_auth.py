import pytest
from auth import authSystem


auth = authSystem()
def test_sign_up():
    assert auth.sign_up("user4", "password4") == "Sign up berhasil"

def tes_sign_up_with_existing_user():
    assert auth.sign_up("user1", "password1") == "Username sudah digunakan, silahkan masukan username lain"

def test_sign_in():
    assert auth.sign_in("user1", "password1") == "Masuk berhasil"


def test_wrong_username():
    assert auth.sign_in("user1", "password_wrong") == "Password salah"

def test_wrong_password():
    assert auth.sign_in("user_not_exist", "password") == "Username tidak ditemukan"

