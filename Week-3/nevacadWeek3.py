# # Salah satu tipe array, array assosiatif
# nama_orang = {
#     "din" : "udin",
#     "angka" : 100,
#     "array" : [1,2,3,4,5],
# }

# array2 = [1,2,3,4,5]
# print(array2[1])

# # OPERATOR LENGTH (LEN)

# panjang = len(nama_orang)
# print(panjang)

# V_name = "key1" in nama_orang
# print(V_name)

# key = "din"

# check = key in nama_orang
# print(check)

# key = "bintang"

# check = key in nama_orang
# print(check)

# # OPERATOR GET

# #Mengambil nilai spesifik dari dictionary
# print(nama_orang["array"][3])

# #Mebgambil nilai menggunakan get
# print(nama_orang.get("din", "Key ini tidak ada"))
# print(nama_orang.get("bintang", "Key Bintang tidak ada"))

# # OPERATOR UPDATE

# nama_orang.update({"bintang" : "Bintang Putra"})
# print(nama_orang.get("bintang", "Key Bintang ini tidak ada"))

# # OPERATOR DELETE (DEL)
# print("======sebelum======", [nama_orang])
# print(len(nama_orang))
# del nama_orang["din"]
# print(nama_orang.get("din", "Key din tidak ada"))
# print("======sesudah======", [nama_orang])
# print(len(nama_orang))

# print('='*100)
# print('OPERATOR COPY')
# # OPERATOR Cpoy (COPY)
# copy = nama_orang.copy()
# nama_orang["din"] = "tol"
# print('Original',nama_orang)
# print('Salinan',copy)


# # Nama dictionary
# nama_orang["din"] = "kon"
# print(nama_orang)

# print('='*100)
# print('OPERATOR POP')
# # OPERATOR POP (Mengeluarkan data dari dictionary)
# name = nama_orang.pop('array')
# # POP ITEM
# nama = nama_orang.popitem()
# names = nama_orang.popitem()
# print(name)
# print(nama_orang)
# print(names)


# Looping Dictionaries
data_list ={
    "Rusdi" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "Rehan"  : 'Vero',
    "Ironi" : [828,676,2323,66767,23132,766]
}

# Loop unutk menampilkan Keys
# n_var
keys = data_list.keys()
# for key in data_list:
#     print(key)
# # Loop unutk menampilkan Value/Isi
value = data_list.values()
# for values in data_list:
#     print(value)

# Loop unutk menampilkan Keys dan Values secara bersamaan 
item = data_list.items()
print(item,"\n")

for keys,values in data_list.items():
    print(keys,values)

# Perhitungan dengan dictionary
pertambahan = sum(data_list['Rusdi'])
panjangValues = len(data_list['Rusdi'])
print(panjangValues)
print(pertambahan)


# Dictionary bersarang atau dalam dictionary ada dictionary
Jeki ={
    'Nama' : 'Arya Zaka',
    'Kelas' : 'XI SIJA 1',
    'Sikap' : 'Buruk'
}

Arkan ={
    'Nama' : 'Arkan',
    'Kelas' : 'XI SIJA 1',
    'Sikap' : 'Baik'
}

Bugar ={
    'Nama' : 'Bugar',
    'Kelas' : 'XI SIJA 1',
    'Sikap' : 'Cukup baik'
}


Putra ={
    'Nama' : 'Putra',
    'Kelas' : 'XI SIJA 1',
    'Sikap' : 'Baik'
}

Yosua ={
    'Nama' : 'Yosua',
    'Kelas' : 'XI SIJA 1',
    'Sikap' : 'Sempurna'
}

siswa={
    'key1': Jeki,
    'key2': Arkan,
    'key3': Bugar,
    'key4': Putra,
    'key5': Yosua,
    
}

# print(f"{'Nama':, 6} {'Kelas':, 10} {'Sikap':, 10}")

# for murid in siswa:
#     Nama = siswa[murid]["Nama"]
#     Kelas = siswa[murid]["Kelas"]
#     Sikap = siswa[murid]["Sikap"]
# print(f"{'Nama':, 6} {'Kelas':, 10} {'Sikap':, 10}")

print(f"{'Nama':<10} {'Kelas':<15} {'Sikap':<30}")

for murid in siswa :
    sis = murid
    Nama = siswa[murid]["Nama"]
    kelas = siswa[murid]["Kelas"]
    Sikap = siswa[murid]["Sikap"]
    print(f"{Nama:<10} {kelas:<15} {Sikap:<30}")




