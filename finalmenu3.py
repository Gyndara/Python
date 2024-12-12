# Input nilai N dari user
N = int(input("Masukkan nilai N: "))

# Inisialisasi variabel
S = 0
pembilang_sebelumnya = 2
penyebut_sebelumnya = 3

# Tampilkan deretnya
deret = "2/3"  # Mulai dengan suku pertama yang sudah diketahui
S += pembilang_sebelumnya / penyebut_sebelumnya

n = 2  # Mulai dari suku kedua

while n <= N:
    # Hitung pembilang berdasarkan rumus (2^(n-1))^2
    pembilang = (2 ** (n - 1)) ** 2
    if n % 2 == 0:
        pembilang += 1  # Untuk N genap, tambahkan 1

    # Hitung penyebut
    penyebut = pembilang_sebelumnya + pembilang

    # Tentukan tanda bergantian (positif-negatif)
    if n % 2 == 0:
        S -= pembilang / penyebut  # Tanda negatif untuk suku genap
        deret += f" - {pembilang}/{penyebut}"
    else:
        S += pembilang / penyebut  # Tanda positif untuk suku ganjil
        deret += f" + {pembilang}/{penyebut}"

    # Update pembilang dan penyebut sebelumnya untuk iterasi berikutnya
    pembilang_sebelumnya = pembilang
    penyebut_sebelumnya = penyebut
    
    n += 1  # Pindah ke suku berikutnya

# Tampilkan hasil perhitungan dan deret
print(f"S = {deret}")
print(f"  = {S:.3f}")
