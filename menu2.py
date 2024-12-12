# Program menghitung suku ke-N dari Fibonacci
# I.S.: Pengguna memasukkan nomor suku ke-N dari Fibonacci
# F.S.: Menampilkan perhitungan suku ke-N dari Fibonacci

# Input dari pengguna
print('-----------------------------------------------------')
print('<<< MASUKKAN NOMOR SUKU FIBONACCI YANG DIINGINKAN >>>')
print('-----------------------------------------------------')

N = int(input("Suku ke: "))

# Validasi input
while (N <= 0):
    print("Masukkan bilangan positif.")
    N = int(input("Masukkan nomor suku Fibonacci yang diinginkan: "))

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
