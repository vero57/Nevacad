XISIJA1 = ['Ayu', 'Dafiq', 'Aldante', 'Arya Pramudia', 'Arya Zaka', 'Ashalia', 'Bugar', 'Chelsi', 'Citra', 'Damar', 'Akmal', 'Farrel', 'Fathir', 'Ilham', 'Kanz', 'Putra', 'Arkan', 'Deni', 'Ryu', 'Bintang', 'Nadhir', 'Nadine', 'Nofrion', 'Nova', 'Putri', 'Ica', 'Aji', 'Iki', 'Sasqia', 'Satya', 'Ghina', 'Taufeil', 'Tiara', 'Wahyu', 'Yosua']
banyak_siswa = len(XISIJA1)
print(banyak_siswa)
# XISIJA1.insert(35, 'Ashrof')
# print(XISIJA1)


# Menambah Data ke list
XISIJA1.append('Dicky')

anak_baru = ['Fuad', 'Rusdi', 'Rehan Bogor']
XISIJA1.extend(anak_baru)
print("="*50)

# Menambah juga
XISIJA1[2] = 'Dipik'

# Menghapus Data pada list
XISIJA1.remove('Dipik')

# Menghapus Data terakhir
XISIJA1.pop()



for i in XISIJA1:
      print(i)

# data_range = range(1, 11)
# print(data_range)
# data_list = list(data_range)
# print(data_list)




