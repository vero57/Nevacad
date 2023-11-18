import pytest

def bagi(angka1, angka2):
    return angka1 / angka2

def test_bagi():
    assert bagi(2, 2) == 1
    assert bagi(4, 2) == 2
    assert bagi(10, 10) == 1