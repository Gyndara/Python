def InputX():
    x = int(input('Masukkan nilai: '))
    return x

def MenghitungX(input_Func):
    x = input_Func()
    hasil = 1
    for i in range(x, 0, -1):
        hasil = hasil * i
        print(i, end='')
        if (i > 1):
            print('x', end='')
    print(f' = {hasil}')

def MenghitungX2(input_Func):
    x = input_Func()
    hasil2 = x * 2
    print(hasil2)

def MenampilkanX2(Tampil_Funcx):
    print('Nilai x + 2')
    Tampil_Funcx(InputX)
MenampilkanX2(MenghitungX2)
        
def MenampilkanX(Tampil_Func):
    print('Hasil faktorial')
    Tampil_Func(InputX)
MenampilkanX(MenghitungX)