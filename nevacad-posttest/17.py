class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis

    def suara(self):
        print("Suaranya mantap")

class Kitsune(Hewan):
    def __init__(self, jenis, ras):
        Hewan.__init__(self, jenis)
        self.ras = ras

    def kebiasaan(self):
        print("Melayani majikannya")

peliharaan = Kitsune("Kitsune", "Rubah")
peliharaan.suara()
peliharaan.kebiasaan()
