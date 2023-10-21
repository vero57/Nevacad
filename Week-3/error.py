while True:
    angka = int(input('Masukan angka: '))



    try:
        bagi = 10/angka
        print(bagi)
        selesai = input('Udahan atau lanjut? ketik "udah" atau "lanjut": ')
        if selesai == 'udah':
            break

        elif selesai != 'lanjut':
            print('YANG BENER LAH GOBLOK')
            
    except:
        print('input tidak sesuai')
    
