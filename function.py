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
        
def MenampilkanX(Tampil_Func):
    print('Hasil faktorial')
    Tampil_Func(InputX)
    
MenampilkanX(MenghitungX)