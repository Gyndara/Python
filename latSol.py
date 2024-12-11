Nama = input('Masukkan nama : ')
Password = int(input('Masukan Nim : '))
if (Password != 10124185):
    for i in range(3):
        Nama = input('Masukkan nama : ')
        Password = int(input('Masukan Nim : '))
else:
    Merek = input('Masukkan merek motor : ')
    Harga = float(input('Masukkan harga motor : '))
    Cicilan = int(input('Masukkan lama cicilan : '))
    Dp = float(input('Masukkan DP: '))
    
    if (Cicilan == 11):
        BayarAngsuran = (0.2653 * Harga + Harga - Dp) / Cicilan
        TotalHarga = (Harga * 0.2653) + (Harga - Dp)
        TotalHarga = TotalHarga - BayarAngsuran
        print('Merek motor  : ', Merek)
        print('Lama cicilan : ', Cicilan)
        print('Bayaran Perbulan : ', BayarAngsuran)
        for i in range(1, Cicilan+1):
            print(f'Bayar {TotalHarga:.0f}  Bulan ke-', i)
            TotalHarga = TotalHarga - BayarAngsuran
    else:
        if (Cicilan == 17):
            BayarAngsuran = (0.3550 * Harga + Harga - Dp) / Cicilan
            TotalHarga = (Harga * 0.3550) + (Harga - Dp)
            TotalHarga = TotalHarga - BayarAngsuran
            print('Merek motor  : ', Merek)
            print('Lama cicilan : ', Cicilan)
            print('Bayaran Perbulan : ', BayarAngsuran)
            for i in range(1, Cicilan+1):
                print(f'Bayar {TotalHarga:.0f}  Bulan ke-', i)
                TotalHarga = TotalHarga - BayarAngsuran
        else:
            if (Cicilan == 23):
                BayarAngsuran = (0.3796 * Harga + Harga - Dp) / Cicilan
                TotalHarga = (Harga * 0.3796) + (Harga - Dp)
                TotalHarga = TotalHarga - BayarAngsuran
                print('Merek motor  : ', Merek)
                print('Lama cicilan : ', Cicilan)
                print('Bayaran Perbulan : ', BayarAngsuran)
                for i in range(1, Cicilan+1):
                    print(f'Bayar {TotalHarga:.0f}  Bulan ke-', i)
                    TotalHarga = TotalHarga - BayarAngsuran
        
