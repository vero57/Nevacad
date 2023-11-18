def bagi_angka(angka1, angka2):
    try:
        hasil = angka1 / angka2
    except:
        return "Error: Pembagian dengan nol!"
    else:
        return hasil

print(bagi_angka(10, 2))  # benar dan akan menghasilkan hasil
print(bagi_angka(10, 0))  # Error karena bagi dengan 0
