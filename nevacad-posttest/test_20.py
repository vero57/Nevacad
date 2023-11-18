import pytest

def kurang(angka1, angka2):
    return angka1 - angka2

def test_kurang():
    assert kurang(2, 2) == 0
    assert kurang(5, 2) == 3
    assert kurang(10, 10) == 0