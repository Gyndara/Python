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
        if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
            Hasil = NilaiA + NilaiB
            print(f'{NilaiA:.0f} + {NilaiB:.0f} = ', Hasil)
        else:
            if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                Hasil = NilaiA + NilaiB
                print(f'{NilaiA:.2f} + {NilaiB:.2f} = {Hasil:.2f}')
    else:
        if(Operator == '-'):
            if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                Hasil = NilaiA - NilaiB
                print(f'{NilaiA:.0f} - {NilaiB:.0f} = ', Hasil)
            else:
                if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                    Hasil = NilaiA - NilaiB
                    print(f'{NilaiA:.2f} - {NilaiB:.2f} = {Hasil:.2f}')
        else:
            if(Operator == 'x'):
                if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                    Hasil = NilaiA * NilaiB
                    print(f'{NilaiA:.0f} x {NilaiB:.0f} = ', Hasil)
                else:
                    if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                        Hasil = NilaiA * NilaiB
                        print(f'{NilaiA:.2f} x {NilaiB:.2f} = {Hasil:.2f}')
            else:
                if(Operator == ':'):
                    if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                        Hasil = NilaiA / NilaiB
                        print(f'{NilaiA:.0f} : {NilaiB:.0f} = ', Hasil)
                    else:
                        if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                            Hasil = NilaiA / NilaiB
                            print(f'{NilaiA:.2f} : {NilaiB:.2f} = {Hasil:.2f}')
    UlangiKalkulator = input('Ulangi perhitungan [Y/T] : ').upper()
    os.system('cls')