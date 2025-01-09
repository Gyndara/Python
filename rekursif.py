
def MenuPilihan():
    print('Menu Pilihan')
    print('1. A pangkat B')
    print('2. Barisan 1,3,3,6,18,24')
    Pilih = int(input('Masukkan Menu Pilihan : '))
    while (Pilih < 0) or (Pilih > 2):
        print('Menu pilihan tidak ada, masukkan ulang...')
        Pilih = int(input('Masukkan Menu Pilihan : '))
    return Pilih

def IsiAB():
    A = int(input('Masukkan nilai A : '))
    B = int(input('Masukkan nilai B : '))
    while (B < 0):
        print('Nilai B tidak boleh kurang dari nol, masukkan ulang...')
        B = int(input('Masukkan nilai B : '))
    return A, B

def Pangkat(A, B):
    if (B == 0):
        return 1
    else:
        if (B == 1):
            return A
        else:
            return A * Pangkat(A, B-1)

def TampilAPangkatB():
    A, B = IsiAB()
    Hasil = Pangkat(A, B)
    print(f'{A} Pangkat {B} = {Hasil}')

def BanyakSuku():
    N = int(input('Masukkan banyak baris : '))
    while (N <= 0):
        print('nilai tidak boleh kurang dari 1, masukkan ulang...')
        N = int(input('Masukkan banyak baris : '))
    return N

def SukuKeN(N):
    if (N == 1):
        return 1
    else:
        if (N == 2):
            return 3
        else:
            if (N % 2 == 1):
                return SukuKeN(N-2) * SukuKeN(N-1)
            else:
                return SukuKeN(N-2) + SukuKeN(N-1)

def TampilBarisan():
    N = BanyakSuku()
    for i in range(1, N + 1):
        if i < N:
            print(SukuKeN(i), end=', ') 
        else:
            print(SukuKeN(i), end='')  
    print() 

def TampilMenuUtama():
    Pilih = MenuPilihan()
    while (Pilih != 0):
        match Pilih:
            case 1:
                TampilAPangkatB()
            case 2:
                TampilBarisan()
        Pilih = MenuPilihan()


TampilMenuUtama()