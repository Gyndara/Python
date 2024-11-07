import os
print('_______________________________________________________')
print('|_______________KASIIR PENJUALAN KANTIN_______________|')
print('|__Kode barang__|____Nama Barang___|___Harga Satuan___|')
print('|_______________|__________________|__________________|')
print('|  PK01         | Pakaian          | Rp.75.000,-      |')
print('|--+------------|------------------|------------------|')
print('|  TS02         | Tas              | Rp.65.000,-      |')
print('|---------------|------------------|------------------|')
print('|  SP03         | Sepatu           | Rp.157.000,-     |')
print('|---------------|------------------|------------------|')
print('|  AK04         | Aksesoris        | Rp.45.000,-      |')
print('|_______________|__________________|__________________|')

KodeProduk = str(input('Masukan kode produk : ')).upper()

if (KodeProduk != 'PK01') and (KodeProduk != 'TS02') and (KodeProduk != 'SP03') and (KodeProduk != 'AK04'):
    print('Produk yang anda masukan tidak terdapat pada toko')
else:
    print(f'Produk {KodeProduk} ada pada toko')

JumlahProduk = int(input('Masukan Jumlah produk : '))

Diskon = 0
StatusDiskon = 'T'

# Meminta input diskon jika jumlah produk >= 12
if (JumlahProduk >= 12):
    StatusDiskon = input('Ada Diskon [Ya/Tidak] : ').upper()

# Jika ada diskon
if (StatusDiskon == 'Y'):
    Diskon = int(input('Besar Diskon : '))
    StatusDiskon = 'Y'

# Menentukan harga satuan dan nama barang berdasarkan kode produk
if (KodeProduk == 'PK01'):
    NamaBarang = 'Pakaian'
    HargaSatuan = 75000
else:
    if (KodeProduk == 'TS02'):
        NamaBarang = 'Tas'
        HargaSatuan = 65000
    else:
        if (KodeProduk == 'SP03'):
            NamaBarang = 'Sepatu'
            HargaSatuan = 157000
        else:
            if (KodeProduk == 'AK04'):
                NamaBarang = 'Aksesoris'
                HargaSatuan = 45000

HargaTotal = JumlahProduk * HargaSatuan
BesaranDiskon = (Diskon / 100) * HargaTotal
TotalBayar = HargaTotal - BesaranDiskon

Bayar = float(input('Masukan jumlah uang : '))
UangKembali = Bayar - TotalBayar

os.system('pause')
os.system('cls')

# Menampilkan detail transaksi
print('Kode Barang     : ', KodeProduk)
print('Nama Barang     : ', NamaBarang)
print('Jumlah Barang   : ', JumlahProduk)
print('Status Diskon   : ', StatusDiskon)
print(f'Harga Satuan    :  Rp.{HargaSatuan:,.0f}')
print(f'Harga Total     :  Rp.{HargaTotal:,.0f}')
print(f'Diskon {Diskon}%       :  Rp.{BesaranDiskon:,.0f}')  
print('_____________________________')
print(f'Total Bayar     :  Rp.{TotalBayar:,.0f}')  
print(f'Bayar           :  Rp.{Bayar:,.0f}')
print(f'Uang Kembalian  :  Rp.{UangKembali:,.0f}')
