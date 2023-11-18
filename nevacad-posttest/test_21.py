import pytest

def kali(angka1, angka2):
    return angka1 * angka2

def test_kali():
    assert kali(2, 2) == 4
    assert kali(5, 2) == 10
    assert kali(10, 10) == 100