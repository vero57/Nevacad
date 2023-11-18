class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info_mobil(self):
        print("Merk Mobil:", self.merk)
        print("Tahun Produksi:", self.tahun)

mobilku = Mobil("Nissan", 2024)
mobilku.info_mobil()
