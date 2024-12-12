import os


UlangiMenu3 = 'Y'
while (UlangiMenu3 == 'Y'):
    print('=====================================================')
    print('<<<           Perhitungan nilai suku-N            >>>')
    print('=====================================================')
    # Validasi input untuk N
    N = -1
    while (N <= 0):
        N = int(input('Banyak suku (N) : '))
        if (N <= 0):
            print('N harus bilangan bulat positif silahkan coba lagi!')

    total = 0
    Operatorminus = False  # Dimulai dengan operator + 
    NilaS = ""  # Untuk menyimpan nilai-s perhitungan

    # Input nilai suku dan perhitungan
    for i in range(1, N + 1):
        valid = False
        while (not valid):
            Suku = input(f'Nilai suku ke-{i} : ')
            if ('/' in Suku):
                # Memisahkan pembilang dan penyebut
                Pembilang, Penyebut = Suku.split('/')
                Pembilang = float(Pembilang)
                Penyebut = float(Penyebut)
                # Validasi penyebut tidak nol
                if (Penyebut == 0):
                    print('Penyebut tidak boleh nol! Silahkan masukkan ulang.')
                else:
                    # Menghitung nilai pecahan
                    nilai_suku = Pembilang / Penyebut
                    # Menambahkan/mengurangkan ke total sesuai operator
                    if (Operatorminus):
                        total -= nilai_suku
                        NilaS += f" - {int(Pembilang)}/{int(Penyebut)}"
                    else:
                        total += nilai_suku
                        if (NilaS == ""):  # Untuk suku pertama tanpa operator
                            NilaS += f"{int(Pembilang)}/{int(Penyebut)}"
                        else:
                            NilaS += f" + {int(Pembilang)}/{int(Penyebut)}"

                    # Berpindah operator
                    Operatorminus = not Operatorminus
                    valid = True
            else:
                print('Penulisan tidak valid! Contoh penulisan: 2/5')
    os.system('cls')

    # Menampilkan hasil akhir dan ekspresi
    print('Banyak suku (N) =', N)
    print(f"S = {NilaS}")
    print(f"  = {total:.3f}")
    UlangiMenu3 = input('Ulangi perhitungan banyak suku-n [Y/T] : ').upper()
    os.system('cls')
