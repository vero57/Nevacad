# OOP DASAR CLASS DAN OBJEK 

# class jomok:
#     pass

# zomok = jomok()
# zomok2 = jomok()

# zomok.name = 'Zaka'
# zomok.jenis = 'Manusia'
# zomok.ciriciri = 'Jomok, Tinggi, sangat jomok, cinta wahyu, sering menggoda wahyu, kakak nevtik'

# print(zomok.__dict__)


# Penggunaan INIT
# class zaka:
#     def __init__(self, x):
#         print('zaka jomok', x)
# joemok = zaka('pencinta wahyu')


# class kendaraan:
#     def __init__(self, jenis, roda):
#         self.jenis = jenis
#         self.roda = roda
# mobil = kendaraan('Mobil', 4)
# motor = kendaraan('Motor', 2)

# print(motor.__dict__, mobil.__dict__)
# print(motor.jenis)


# class buah:
#     def __init__(self, namaBuah, jenisBuah):
#         self.namaBuah = namaBuah
#         self.jenisBuah = jenisBuah
# duren = buah('Duren', 'Buah-Buahan')
# tomat = buah('Tomat', 'Sayuran')

# print(duren.__dict__, tomat.__dict__)



# class hero:
#     jumlah_hero = 0
#     def __init__(self, nama, power, darah):
#         # instance variables
#         self.nama = nama
#         self.power = power
#         self.darah = darah
#         hero.jumlah_hero += 1

#     # Methon tanpa argumen dan tanpa return
#     def namaku(self):
#         print("Namaku adalah ", self.nama)
#     # Method dengan argumen dan tanpa return
#     def darahUp(self, up):
#         self.darah += up
#     # Method dengan return
#     def darahGet(self):
#         return self.darah

# hero1 = hero('HuTao', 1000, 25000)
# hero2 = hero('Qiqi', 200, 1000)
# hero3 = hero('Keqing', 99999999999999999999999999999999999999999999999999999999999999999, 1)
# print(hero.jumlah_hero)
# print('Darahku sekarang ', hero1.darahGet())
# hero1.namaku()
# hero1.darahUp(10)


# print('='*100)


# print('aku mendapatkan heal dan darahku sekarang', hero1.darahGet())
# print('Nama', hero1.nama, 'Power', hero1.power, 'Darah', hero1.darah)
# print('Nama', hero2.nama, 'Power', hero2.power, 'Darah', hero2.darah)
# print('Nama', hero3.nama, 'Power', hero3.power, 'Darah', hero3.darah)



# class senjata:
#     def __init__(self, namas, jeniss):
#         self.namas = namas
#         self.jeniss = jeniss

# senjata1 = senjata('Staff of Homa', 'Tombak')
# senjata2 = senjata('Skyward', 'Buku sihir')

# print('Nama Weapon', senjata1.namas, 'Jenis senjata', senjata1.jeniss)


# class segitiga:
#     def __init__(self, alas, tinggi, sisi):
#         self.alas = alas
#         self.tinggi = tinggi
#         self.sisi = sisi
    
#     def getluas(self):
#         return 0.5 * self.alas * self.tinggi

#     def getkeliling(self):
#         return self.alas + self.sisi + self.sisi


# segitiga1 = segitiga(121, 20, 50)
# print('Luas segitiga', segitiga1.getluas())
# print('Keliling segitiga', segitiga1.getkeliling())



# class kubus:
#     def __init__(self, sisis):
#         self.sisis = sisis
#     def volume(self):
#         return self.sisis^3
# kubus1 = kubus(200)

# print('Volume ajah', kubus1.volume())


# class lingkaran:
#     def __init__(self, diameter):
#         self.diameter = diameter
    
#     def get_diameter(self):
#         return 3.14 * self.diameter * self.diameter
# lingkaran1 = lingkaran(14)
# print('Luas lingkaran asalah', lingkaran1.get_diameter()) 



class hero:
    jumlah = 0


    def __init__(self, nama, power, darah):
        self.__nama = nama
        self.__power = power
        self.__darah = darah
        hero.jumlah += 1

    # Private instance variable
        self._private = "Private"

# Getter (Variabel yang tidak bisa diubah)
    def getNama(self):
        return self.__nama
    def getPower(self):
        return self.__power
    def getDarah(self):
        return self.__darah

# Setter (Variabel yang bisa diubah)
    def diserang(self, kekuatanserang):
        self.__darah -= kekuatanserang
hero1 = hero('Saber', 100, 200)
print(hero1.getNama())
print(hero1.getPower())
hero1.diserang(2)
print(hero1.getDarah())



# Pewarisan
class hewan:
    def __init__(self, nama, jenis, kaki, habitat):
        self.nama = nama
        self.jenis = jenis
        self.kaki = kaki
        self.habitat = habitat

class hewan_mamalia(hewan):
    pass
paus = hewan('Lele', 'Ikan', 0, 'air')
monyet = hewan('Monyet', 'Unggas', 100, 'hutan')

print(paus.__dict__)
print(monyet.__dict__)



# OOP coba coba kak citra
while True:
    class kubus:
        def __init__(self, sisi):
            self.sisi = sisi
        def volume(self):
            return self.sisi**3
    kubus = kubus(int(input('Sisi kubus: ')))
    print('Luas kubus adalah: ', kubus.volume())
