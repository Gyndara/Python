# Program menu pilihan
# I.S.: Pengguna memasukan salah satu angka pilihan untuk menu (1/2/3/4/0)
# F.S.: Menampilkan menu sesuai dengan input pengguna

import os

# badan program
print('                                            ======================================')
print('                                            ||           SELAMAT DATANG         ||')
print('                                            ||==================================||')
print('                                            ||        PROGRAM MENU PILIHAN      ||')
print('                                            ||==================================||')
print('                                            ||             KELOMPOK 1           ||')
print('                                            ||==================================||')
print('                                            ||SEMESTER-1                    2024||')
print('                                            ======================================')
os.system('pause')
os.system('cls')

# Menu pilihan
print('========================================')
print('||            Menu Pilihan            ||')
print('========================================')
print('|| 1. Kalkulator sederhana            ||')
print('||====================================||')
print('|| 2. Suku ke-N dari deret fibonacci  ||')
print('||====================================||')
print('|| 3. S = 2/3 - 5/7 + 16/21...        ||')
print('||====================================||')
print('|| 4. Anggota kelompok                ||')
print('||====================================||')
print('|| 0. Keluar                          ||')
print('========================================')

# Pengguna memasukkan nilai ururtan sesuai dengan menu yang dipilih
Pilih = int(input('Masukan angka menu pilihan anda : '))
while(Pilih != 0):
    os.system('cls')
    match(Pilih):
        case 1:
            UlangiMenu1 = 'Y'
            while(UlangiMenu1 == 'Y'): 
                print('=====================================================')
                print('<<<             KALKULATOR SEDERHANA              >>>')
                print('=====================================================')
                NilaiA = float(input('Masukkan angka ke-1         : '))
                NilaiB = float(input('Masukkan angka ke-2         : '))
                Operasi = input('Pilih Operasi [+/-/x/:]     : ')

                #validasi apakah operasi sesuai
                while(Operasi != '+') and (Operasi != '-') and (Operasi != 'x') and (Operasi != ':'):
                    print('Operasi yang tersedia hanya [+/-/x/:], tekan enter untuk pilih ulang Operasi....')
                    os.system('pause')
                    os.system('cls')
                    print('=====================================================')
                    print('<<<             KALKULATOR SEDERHANA              >>>')
                    print('=====================================================')
                    print(f'Nilai A :  {NilaiA:.0f}')
                    print(f'Nilai B :  {NilaiB:.0f}')
                    Operasi = input('Pilih Operasi [+/-/x/:] : ')
            
                if(Operasi == '+'):
                    if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                        Hasil = NilaiA + NilaiB
                        print(f'Hasil =  {NilaiA:.0f} + {NilaiB:.0f}')
                        print(f'      =  {Hasil:.1f}')
                    else:
                        if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                            Hasil = NilaiA + NilaiB
                            print(f'Hasil = {NilaiA:.2f} + {NilaiB:.2f}')
                            print(f'      = {Hasil:.2f}')
                else:
                    if(Operasi == '-'):
                        if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                            Hasil = NilaiA - NilaiB
                            print(f'Hasil =  {NilaiA:.0f} - {NilaiB:.0f}')
                            print(f'      =  {Hasil:.1f}')
                        else:
                            if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                                Hasil = NilaiA - NilaiB
                                print(f'Hasil = {NilaiA:.2f} - {NilaiB:.2f}')
                                print(f'      = {Hasil:.2f}')
                    else:
                        if(Operasi == 'x'):
                            if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                                Hasil = NilaiA * NilaiB
                                print(f'Hasil =  {NilaiA:.0f} x {NilaiB:.0f}')
                                print(f'      =  {Hasil:.1f}')
                            else:
                                if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                                    Hasil = NilaiA * NilaiB
                                    print(f'Hasil = {NilaiA:.2f} x {NilaiB:.2f}')
                                    print(f'      = {Hasil:.2f}')
                        else:
                            if(Operasi == ':'):
                                if(NilaiA == int(NilaiA)) and (NilaiB == int(NilaiB)):
                                    Hasil = NilaiA / NilaiB
                                    print(f'Hasil =  {NilaiA:.0f} : {NilaiB:.0f}')
                                    print(f'      =  {Hasil:.1f}')
                                else:
                                    if(NilaiA == float(NilaiA)) and (NilaiB == float(NilaiB)):
                                        Hasil = NilaiA / NilaiB
                                        print(f'Hasil = {NilaiA:.2f} : {NilaiB:.2f}')
                                        print(f'      = {Hasil:.2f}')
                UlangiMenu1 = input('Ulangi perhitungan [Y/T] : ').upper()
                os.system('cls')
                if (UlangiMenu1 == 'T'):
                    # Menu pilihan
                    print('========================================')
                    print('||            MENU PILIHAN            ||')
                    print('========================================')
                    print('|| 1. Kalkulator sederhana            ||')
                    print('||====================================||')
                    print('|| 2. Suku ke-N dari deret fibonacci  ||')
                    print('||====================================||')
                    print('|| 3. S = 2/3 - 5/7 + 15/21...        ||')
                    print('||====================================||')
                    print('|| 4. Anggota kelompok                ||')
                    print('||====================================||')
                    print('|| 0. Keluar                          ||')
                    print('========================================')
                    # Pengguna memasukkan nilai ururtan sesuai dengan menu yang dipilih
                    Pilih = int(input('Masukan angka menu pilihan anda : '))
                    os.system('cls')
        case 2:
            # Input dari pengguna
            print('-----------------------------------------------------')
            print('<<<          PERHITUNGAN SUKU FIBONACCI           >>>')
            print('-----------------------------------------------------')

            N = int(input("Suku ke: "))

            # Validasi input
            while (N <= 0):
                print('-----------------------------------------------------')
                print('<<<          PERHITUNGAN SUKU FIBONACCI           >>>')
                print('-----------------------------------------------------')

                N = int(input("Suku ke: "))
                os.system('cls')

            # Inisialisasi
            Suku1 = 0
            Suku2 = 1  
            Suku_N = 2  

            # Perhitungan Fibonacci menggunakan while
            if (N == 1):  
                Hasil = Suku1
            elif (N == 2):  
                Hasil = Suku2
            else:
                while (Suku_N <= N):  
                    fib = Suku1 + Suku2   
                    Suku1 = Suku2         
                    Suku2 = fib       
                    Suku_N += 1
                Hasil = Suku2  

            # Menampilkan hasil
            print(f"Suku ke-{N} dari deret Fibonacci adalah {Hasil}")
            print('-----------------------------------------------------')
            UlangiMenu2 = input('Ulangi perhitungan suku fibonacci [Y/T] : ').upper()
            os.system('cls')
            if (UlangiMenu2 == 'T'):
                # Menu pilihan
                print('========================================')
                print('||            MENU PILIHAN            ||')
                print('========================================')
                print('|| 1. Kalkulator sederhana            ||')
                print('||====================================||')
                print('|| 2. Suku ke-N dari deret fibonacci  ||')
                print('||====================================||')
                print('|| 3. S = 2/3 - 5/7 + 15/21...        ||')
                print('||====================================||')
                print('|| 4. Anggota kelompok                ||')
                print('||====================================||')
                print('|| 0. Keluar                          ||')
                print('========================================')
                # Pengguna memasukkan nilai ururtan sesuai dengan menu yang dipilih
                Pilih = int(input('Masukan angka menu pilihan anda : '))
                os.system('cls')
        case 3:
            UlangiMenu3 = 'Y'
            while (UlangiMenu3 == 'Y'):
                print('=====================================================')
                print('<<<           PERHITUNGAN NILAI SUKU-N            >>>')
                print('=====================================================')
                # Input nilai N dari user
                N = int(input("Masukkan nilai N: "))

                while (N <= 0):
                    os.system('cls')
                    print('Nilai N tidak boleh 0 dan lebih kecil dari 0')
                    os.system('cls')
                    print('=====================================================')
                    print('<<<           PERHITUNGAN NILAI SUKU-N            >>>')
                    print('=====================================================')
                    # Input nilai N dari user
                    N = int(input("Masukkan nilai N: "))
                # Inisialisasi variabel
                S = 0
                PembilangSebelum = 2
                PenyebutSebelum = 3

                deret = "2/3"  # nilai awal
                S += PembilangSebelum / PenyebutSebelum

                i = 2  # Mulai dari suku kedua

                while i <= N:
                    #rumus (2^(n-1))^2
                    pembilang = (2 ** (i - 1)) ** 2
                    if i % 2 == 0:
                        pembilang += 1  
                    penyebut = PembilangSebelum + pembilang

                    if i % 2 == 0:
                        S -= pembilang / penyebut 
                        deret += f" - {pembilang}/{penyebut}"
                    else:
                        S += pembilang / penyebut  
                        deret += f" + {pembilang}/{penyebut}"

                    PembilangSebelum = pembilang
                    PenyebutSebelum = penyebut
                    i += 1  

                # menampilkan hasil perhitungan dan deret
                print(f"S = {deret}")
                print(f"  = {S:.3f}")

                UlangiMenu3 = input('Ulangi perhitungan banyak suku-n [Y/T] : ').upper()
                os.system('cls')
                if (UlangiMenu3 == 'T'):
                    # Menu pilihan
                    print('========================================')
                    print('||            MENU PILIHAN            ||')
                    print('========================================')
                    print('|| 1. Kalkulator sederhana            ||')
                    print('||====================================||')
                    print('|| 2. Suku ke-N dari deret fibonacci  ||')
                    print('||====================================||')
                    print('|| 3. S = 2/3 - 5/7 + 15/21...        ||')
                    print('||====================================||')
                    print('|| 4. Anggota kelompok                ||')
                    print('||====================================||')
                    print('|| 0. Keluar                          ||')
                    print('========================================')
                    # Pengguna memasukkan nilai urutan sesuai dengan menu yang dipilih
                    Pilih = int(input('Masukan angka menu pilihan anda : '))
                    os.system('cls')
        case 4:
            print('==================================================')
            print('||                   KELOMPOK 1                 ||')
            print('==================================================')
            print('|No|              NAMA              ||    NIM   ||')
            print('==================================================')
            print('|1.| Andreana Rahmawan              || 10124168 ||')
            print('==================================================')
            print('|2.| Bisma Gyndara Mages Jayalangit || 10124185 ||')
            print('==================================================')
            print('|3.| Rania                          || 10124196 ||')
            print('==================================================')
            print('|4.| Farhan Naufal Ardiansyah       || 10124198 ||')
            print('==================================================')

            Menu = input('Pilih Menu lainnya [Y/T] : ').upper()
            os.system('cls')
            if(Menu == 'Y'):
                    # Menu pilihan
                    print('========================================')
                    print('||            Menu Pilihan            ||')
                    print('========================================')
                    print('|| 1. Kalkulator sederhana            ||')
                    print('||====================================||')
                    print('|| 2. Suku ke-N dari deret fibonacci  ||')
                    print('||====================================||')
                    print('|| 3. S = 2/3 - 5/7 + 15/21...        ||')
                    print('||====================================||')
                    print('|| 4. Anggota kelompok                ||')
                    print('||====================================||')
                    print('|| 0. Keluar                          ||')
                    print('========================================')
                    # Pengguna memasukkan nilai urutan sesuai dengan menu yang dipilih
                    Pilih = int(input('Masukan angka menu pilihan anda : '))
                    os.system('cls')
            else:
                Pilih = 0
    
