#BISMA GYNDARA MAGES JAYALANGIT

print('____________________________________________')
print('|__________KASIIR PENJUALAN KANTIN_________|')
print('|_______Nama barang________|_____Harga_____|')
print('|__________________________________________|')
print('| 1. Bala-bala             | Rp.2000       |')
print('|------------------------------------------|')
print('| 2. Gehu                  | Rp.3000       |')
print('|------------------------------------------|')
print('| 3. Cireng                | Rp.4000       |')
print('|------------------------------------------|')
print('| 4. Lepeut                | Rp.5000       |')
print('|------------------------------------------|')
print('| 5. Air Mineral           | Rp.6000       |')
print('|__________________________________________|')

NamaKasir  = input('Nama Penjaga kasir   : ')
NamaBarang = input('Barang yang dibeli   : ')
Quantity   = int(input('Porsi yang dibeli    : '))

if NamaBarang == 'Bala-bala' or NamaBarang == 'bala-bala' or NamaBarang == 'bala bala' or NamaBarang == 'bala' or NamaBarang == '1':
    pembayaran = Quantity * 2000
    print('Total Pembelian :', pembayaran)
elif NamaBarang == 'Gehu' or NamaBarang == 'gehu' or NamaBarang == '2':
    pembayaran = Quantity * 3000
    print('Total Pembelian :', pembayaran)
elif NamaBarang == 'Cireng' or NamaBarang == 'cireng' or NamaBarang == '3':
    pembayaran = Quantity * 4000
    print('Total Pembelian :', pembayaran)
elif NamaBarang == 'Leupet'or NamaBarang == 'Lepet' or NamaBarang == 'leupet' or NamaBarang == 'lepet' or NamaBarang == '4':
    pembayaran = Quantity * 5000
    print('Total Pembelian :', pembayaran)
elif NamaBarang == 'Air Mineral' or NamaBarang == 'air mneral' or NamaBarang == 'air' or NamaBarang == 'mineral' or NamaBarang == '5':
    pembayaran = Quantity * 6000
    print('Total Pembelian :', pembayaran)
