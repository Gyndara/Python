M = int(input('Masukkan nilai M : '))
if (M < 0) and (M > 20):
    print('Nilai tidak boleh 0 atau lebih dari 20')
N = int(input('Masukkan nilai N : '))
if (N < -5) and (N > 15):
    print('Nilai tidak boleh 0 atau lebih dari 20')

if (M == 0) and (N == 0):
    Kali = 1
    print(Kali)
else:
    if (M == 0):
        Kali = 0
        print(Kali)
    else:
        if (N == 0):
            Kali = 1
            print(Kali)
        else:
            Kali = 1
            for i in range(1, N+1):
                print(M, end='')
                Kali = Kali * M
                if (i < N):
                    print('x', end='')
            print(' = ',Kali)