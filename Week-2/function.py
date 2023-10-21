def halo():
    print("papua merdeka")

halo()

def jomok(nama):
    print("Halo", nama, "Jomok")
jomok("Wahyu")
    
def number(angka):
    return sorted(angka)

print(number([4,2,3,5,1,6,8,7,9,10]))

def add_number(num1, num2):
    print("Angka num1 adalah ",num1, "angka num2 adalah ",num2)
add_number(5, 4)

def halo(n1,n2):
    hasil = n1 + n2
    return hasil
perjumlahan = halo(50,10)
print(f" hasilnya:",perjumlahan)
print ("="*60)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
def luas_kubus(sisi):
    luas = luas_persegi(sisi) * 6
    print(luas)

luas_persegi(3)
luas_kubus(5)













