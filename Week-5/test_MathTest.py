from MathTest import tambah, kurang, kali, bagi, pangkat, ganjil, genap

def test_tambah():
    assert tambah(5, 2) == 7


def test_kurang():
    assert kurang(5,6) == -1


def test_kali():
    assert kali(5,6) == 30

def test_bagi():
    assert bagi(8,2) == 4

def test_pangkat():
    assert pangkat(2,2) == 4


def test_ganjil():
    assert ganjil(3) == 1

def test_genap():
    assert genap(100) == 0