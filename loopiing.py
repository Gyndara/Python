def segitiga_piramida(n):
    i = 0
    while i < n:
        # Menambahkan spasi di kiri dan '*' sesuai baris yang sedang dicetak
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
        i += 1

# Contoh penggunaan
tinggi = 12  # Ganti dengan tinggi segitiga yang diinginkan
segitiga_piramida(tinggi)
