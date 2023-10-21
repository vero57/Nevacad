angka = [1,3,2,4,6,5,7,9,8,10]
print(angka)
# Menghitung jumlah angka 1 pada data
jumlah_data = angka.count(1)
print(jumlah_data)

siswa = ['Akmal', 'Jeki', 'Fathir', 'Yosua']
siswa_index = siswa.index('Jeki')
print("index Jeki adalah",siswa_index)


# Mengurutkan angka dengan sort
print("Data angka sebelum sort",angka)
angka.sort()
print('Sesudah di sort',angka)
siswa.sort()
print(siswa)

print("\n")

# Membalik urutan data
angka.reverse()
siswa.reverse()
print(angka,siswa)

angka = int(input('ankga: '))

if angka % 2 == 0:
    print('Angka yang kamu pilih adalah angka genap')
else:
    print('Angka kamu itu ganjil')
