import pytest

def tambah(angka1, angka2):
    return angka1 + angka2

def test_tambah():
    assert tambah(1, 2) == 3
    assert tambah(-1, 1) == 0
    assert tambah(0, 0) == 0
