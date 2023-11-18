import pytest

def pangkat(angka1, angka2):
    return angka1 ** angka2

def test_pangkat():
    assert pangkat(2, 2) == 4
    assert pangkat(5, 2) == 25
    assert pangkat(10, 2) == 100