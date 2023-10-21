nama = input('Masukan Nama: ')
password = input('Password: ')

if nama == 'admin':
    print('Anda Login Sebagai Admin')
    print('Halo Atmin')
if password != 1:
    print('')
else:
    print('Password salah')


if nama == 'user':
    print('Anda Login Sebagai User')
    print('Welcome')
if password != 2:
    print("password salah")


