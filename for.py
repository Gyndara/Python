N = int(input(' masukan angka : '))

if N == 0 or N == 1:
    Faktorial = 1
else:
    Faktorial = 1
    print(f'{N:>2}! = ', end='')
    for i in range(N, 0, -1):
        print(i, end='')
        if i > 1:
            print(' x ',end='')
        Faktorial *= i
    print(f' = {Faktorial}')