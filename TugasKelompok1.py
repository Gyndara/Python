import os







UlangiKalkulator = 'Y'
while(UlangiKalkulator == 'Y'): 
    print('===========KALKULATOR SEDERHANA===========')
    NilaiA = float(input('Masukkan Nilai A         : '))
    NilaiB = float(input('Masukkan Nilai B         : '))
    Operator = input('Pilih Operator [+/-/x/:] : ')
    os.system('cls')

    while(Operator != '+') and (Operator != '-') and (Operator != 'x') and (Operator != ':'):
        print('Operator yang tersedia hanya [+/-/x/:], tekan enter untuk pilih ulang operator....')
        os.system('pause')
        os.system('cls')
        print(f'Nilai A :  {NilaiA:.0f}')
        print(f'Nilai B :  {NilaiB:.0f}')
        Operator = input('Pilih Operator [+/-/x/:] : ')


    if(Operator == '+'):
        Hasil = NilaiA + NilaiB
        print(f'{NilaiA} + {NilaiB} = ', Hasil)
    else:
        if(Operator == '-'):
            Hasil = NilaiA - NilaiB
            print(f'{NilaiA} - {NilaiB} = ', Hasil)
        else:
            if(Operator == 'x'):
                Hasil = NilaiA * NilaiB
                print(f'{NilaiA} x {NilaiB} = ', Hasil)
            else:
                if(Operator == ':'):
                    Hasil = NilaiA / NilaiB
                    print(f'{NilaiA} : {NilaiB} = ', Hasil)
    UlangiKalkulator = input('Ulangi perhitungan [Y/T] : ').upper()
    os.system('cls')
        
        