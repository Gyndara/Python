import os

def PilihMenu():
    print('Menu pilihan')
    print('1. Kalkulator')
    print('2. Fibonacci')
    print('3. Deret 2/3 - 5/7 + 15/21')
    Pilih = int(input('Masukkan Menu pilihan: '))
    while Pilih <= 0 or Pilih > 3:
        print('Menu tidak ada')
        Pilih = int(input('Masukkan Menu Pilihan: '))
    return Pilih

def TampilMenu(Pilih):
    match Pilih:
        case 1:
            os.system('cls')
            print('Kalkulator sederhana')
            angka1 = int(input('Masukkan angka kesatu = '))
            angka2 = int(input('Masukkan angka kedua = '))
            operator = input('Masukkan operator +/-/x/: = ')
            while operator not in ['+', '-', 'x', ':']:
                print('Operator tidak tersedia, ulangi')
                operator = input('Masukkan operator +/-/x/: = ')
            return angka1, angka2, operator
        case 2:
            os.system('cls')
            print('Suku Fibonacci')
            N = int(input('Masukkan banyak suku-N: '))
            while N <= 0:
                print('Tidak boleh kurang dari 1')
                N = int(input('Masukkan banyak suku-N: '))
            return N
        case 3:
            os.system('cls')
            print('Deret 2/3 - 5/7 + 15/21')
            N = int(input('Masukkan banyak suku-S: '))
            while N <= 0:
                print('Tidak boleh kurang dari 1')
                N = int(input('Masukkan banyak suku-S: '))
            return N

def kalulator(angka1, angka2, operator):
    if operator == '+':
        return angka1 + angka2
    elif operator == '-':
        return angka1 - angka2
    elif operator == 'x':
        return angka1 * angka2
    elif operator == ':':
        return angka1 / angka2 if angka2 != 0 else "Error: Pembagian dengan nol"

def fibonacci(N):
    # Inisialisasi
    Suku1 = 0
    Suku2 = 1  
    Suku_N = 2 
    # Perhitungan Fibonacci menggunakan while
    if (N == 1):  
        hasilFibo = Suku1
    elif (N == 2):  
        hasilFibo = Suku2
    else:
        while (Suku_N <= N):  
            fib = Suku1 + Suku2   
            Suku1 = Suku2         
            Suku2 = fib       
            Suku_N += 1
        hasilFibo = Suku2  
    return hasilFibo

def sukuS(N):
    S = 0
    PembilangSebelum = 2
    PenyebutSebelum = 3
    deret = "2/3"
    S += PembilangSebelum / PenyebutSebelum
    for i in range(2, N + 1):
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
    return S, deret

def TampilHasilKalkulator(angka1, angka2, operator):
    hasil = kalulator(angka1, angka2, operator)
    print(f'Hasil dari {angka1} {operator} {angka2} = {hasil}')

def TampilHasilFibonacci(N):
    hasilFibo = fibonacci(N)
    print(f'Suku ke-{N} dalam deret Fibonacci adalah {hasilFibo}')

def TampilHasilSukuS(N):
    S, deret = sukuS(N)
    print(f"S = {deret}")
    print(f"  = {S:.3f}")

# Pemanggilan Fungsi Utama
Pilih = PilihMenu()
if Pilih == 1:
    angka1, angka2, operator = TampilMenu(Pilih)
    TampilHasilKalkulator(angka1, angka2, operator)
elif Pilih == 2:
    N = TampilMenu(Pilih)
    TampilHasilFibonacci(N)
elif Pilih == 3:
    N = TampilMenu(Pilih)
    TampilHasilSukuS(N)
