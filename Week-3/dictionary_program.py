backpack = {}

while True:
    print("\nSelamat datang sayang!!!")
    print("Sayang mau ngapain, dipilih ya awww")
    print("1. Tampilkan isi")
    print("2. Tambah item(Negro njir)")
    print("3. Hapus item")
    print("4. Ganti item")
    print("5. Keluar ahhhhhhh")
    pilihan = int(input("Masukkan pilihan Anda (1-5): "))
    if pilihan == 1:
        print("Isi saat ini:")
        for barang, jumlah in backpack.items():
            print(f"- {barang} : {jumlah}")
        print(f"Total cum: {sum(backpack.values())}")
    elif pilihan == 2:
        print("Masukkan nama dan jumlah:")
        barang = input("Nama barang: ")
        jumlah = int(input("Jumlah: "))
        if barang in backpack:
            backpack[barang] += jumlah 
        else:
            backpack[barang] = jumlah 
        print(f"Lu nambahin {jumlah} {barang} ke gudang lu.")
    elif pilihan == 3:
        print("Masukkan nama barang yang ingin dihapus:")
        barang = input("Nama barang: ")
        if barang in backpack:
            del backpack[barang] 
            print(f"Lu ngehapus {barang} dari gudang Anda.")
        else:
            print(f"Barang {barang} ga ada di gudang lu.")
    elif pilihan == 4:
        print("Masukkan nama barangnya yang pengen diganti dan nama barang baru :")
        lama = input("Nama barang lama: ")
        baru = input("Nama barang baru: ")
        if lama in backpack:
            jumlah = backpack[lama]
            del backpack[lama]
            backpack[baru] = jumlah
            print(f"Lu ganti {lama} dengan {baru}.")
        else:
            print(f"Barang {lama} gada.")
    elif pilihan == 5:
        break 
    else:
        print("Pilihan gajelas apacoba")
