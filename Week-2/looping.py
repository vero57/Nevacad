a = float(input('Masukan angka pertama:'))
b = float(input('Masukan angka kedua:'))
c = input('Apa yang ingin anda lakukan:')

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == '%':
    print(a % b)
elif c == '^':
    print(a ** b)


a = input('Masukan username: ')
b = input('Masukan password: ')

if a == 'admin' and b == '123':
    print('Login berhasil')
elif a == 'admin' and b != '123':
    print('Password salah')
elif a == 'user' and b == '1234':
    print('Login berhasil')
elif a == 'user' and b!= '1234':
    print('Password salah')
else:
    print('User tidak terdaftar')

i = 1
while i < 10:
    print(i)
    i += 1

sija = ['Akmal', 'Fathir', 'Jeki', 'Putra', 'Bugar']

for i in sija:
    print(i)


while True:
    num = int(input('Masukan angka'))
    print('Kamu memilih angka ',num)




buah = ['Apel', 'Mangga', 'Nanas', 'Duren', 'Singkong']

i = 0

while i < reversed(len(buah)):
    print(buah[i])
    i =- -1



for i in range(10):
    if i == 6:
        break
    print(i)

for i in range(10):
    if i == 3:
        continue
    print(i)


num = 0
while num < 10:
    print(num)
    if num == 5:
        break
    print(num)
    num += 1



num = [20,32,11,34,69,10,59]
genap = []
ganjil = []
for i in num:
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)

print('Ini adalah angka genap ',genap)
print('Ini adalah angka genap ',ganjil)




angka = [1,2,3,4,5,6,7,8,9,10]

for i in angka:
    print(angka)



        