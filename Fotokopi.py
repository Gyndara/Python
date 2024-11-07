#I.S.: pengguna memvalidasi apakah laangganan atau tidak dengan mengisi [Y/T]
#F.S.: menampilkan validasi langganan, jumlah lembar fotokopi, harga satuan, total bayar 

import os
#memasukan nilai [Y/T] untuk memvalidasi apakah langganan atau bukan
langganan = input('Langganan [Y/T] : ').upper()
if langganan != 'Y' and langganan != 'T':
    print('Anda hanya bisa masukan Y atau T')
else:
    print(f'Pilihan Anda: {langganan}')

#memasukan jumlah lembar fotokopi
jumlah = int(input('Jumlah lembar fotokopi : '))

os.system('pause')
os.system('cls')

#menghitung total biaya fotokopi
if (langganan == 'Y'):
    TotalBayar = jumlah * 200
else:
    if(jumlah < 100):
        TotalBayar = jumlah * 300
    else:
        TotalBayar = jumlah * 250
#menghitung harga satuan lembar fotokopi
HargaSatuan = TotalBayar / jumlah

print(' <<<< BIAYA FOTOKOPI >>>>')
print('Langganan [Y/T]        : ', langganan)
print('Jumlah lembar fotokopi : ', jumlah)
print(f'Harga satuan fotokopi  :  Rp.{HargaSatuan:,.0f}')
print(f'Total bayar fotokopi   :  Rp.{TotalBayar:,.0f}')
