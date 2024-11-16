# print('Hasil : ')
# Hasil = 0
# for i in range(1, 11):
#     print(i, end='')
#     Hasil = Hasil + i
#     if (i < 10):
#         print('+', end='')
# print(' = ', Hasil)

# print('Hasil :')
# Hasil = 0
# for i in range(10, 0, -1):
#     print(i, end='')
#     Hasil = Hasil + i
#     if(i > 1):
#         print('+', end='')
# print('= ', Hasil)

NilaiA = int(input('Masukan nilai-N : '))
print('Hasil :')
Hasil = 0
i = 0
while (i < NilaiA):
    print(i, end='')
    Hasil = Hasil + i
    i = i + 1
    if ( i < NilaiA):
        print('+', end='')
print('= ', Hasil)

# print('Hasil :')
# Hasil = 0
# i = 10
# while (i >= 1):
#     print(i, end='')
#     Hasil = Hasil + i
#     i = i - 1
#     if (i >= 1):
#         print('+', end='')
# print(' =', Hasil)


#Bisma Gyndara Mages Jayalangit
#10124185

# M = int(input('Masukan nilai M : '))
# while (M >= 20) or (M < 0):
#     print('Nilai M hanya bisa 20 sampai 0')
#     M = int(input('Masukan nilai M : '))


# N = int(input('Masukan nilai N : '))
# while (N >= 15) or (N <= -5):
#     print('Nilai M : ', M)
#     print('Nilai N hanya bisa 15 sampai -5')
#     N = int(input('Masukan nilai N : '))

# print('Hasil : ')

# if M == 0 or N == 0:
#     kali = 0
#     print(f'{M} x {N} = {kali}')
# elif M == 1:
#     kali = N
#     print(f'{M} x {N} = {kali}')
# else:
#     kali = 0
#     print(f'{M} x {N} = ', end='')
#     for i in range(1, M + 1):
#         print(N, end='')
#         kali += N
#         if i < M:
#             print(' + ', end='')
#     print(f' = {kali}')  # Tampilkan hasil akhir