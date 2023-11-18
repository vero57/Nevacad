class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.__gaji = gaji

    def get_gaji(self):
        return self.__gaji

    def set_gaji(self, gaji):
        self.__gaji = gaji

akmalcorp = Pegawai("Arya Zaka", 10000)
print(akmalcorp.get_gaji())

akmalcorp.set_gaji(5000)
print(akmalcorp.get_gaji())
