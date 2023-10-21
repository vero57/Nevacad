a = float(input('Masukan angka pertama:'))
b = float(input('Masukan angka kedua:'))
c = input('Kamu mau angkanya diapain?:')

print('==='*15)

if c == '+':
    print(a + b)
elif c == '-':
    print(a-b)
elif c == '/':
    print(a/b)
elif c == '*':
    print(a*b)
elif c == '%':
    print(a%b)
elif c == '^':
    print(a**b)