#BISMA GYNDARA MAGES JAYALANGIT

Bulan = input('Masukan Bulan       :')
Tahun = input('Masukan Tahun (yyyy):')

print('-------------------DATA KARYAWAN KESATU---------------------')
Nama1      = input('Masukan Nama        :')
NIK1       = input('Masukan NIK         :')
GajiPokok1 = float(input('Masukan Gaji Pokok  :Rp.'))
PPN1 = 0.1 * GajiPokok1
Tunjangan1 = 0.2 * GajiPokok1
GajiBersih1 = GajiPokok1 + Tunjangan1 - PPN1
formatGajiPokok1 = f'{GajiPokok1:,.0f}'.replace(',','.')
formatPpn1 = f'{PPN1:,.0f}'.replace(',','.')
formatTunjangan1 = f'{Tunjangan1:,.0f}'.replace(',','.')
formatGajiBersih1 = f'{GajiBersih1:,.0f}'.replace(',','.')

print('-------------------DATA KARYAWAN KEDUA---------------------')
Nama2      = input('Masukan Nama        :')
NIK2       = input('Masukan NIK         :')
GajiPokok2 = float(input('Masukan Gaji Pokok  :Rp.'))
PPN2 = 0.1 * GajiPokok2
Tunjangan2 = 0.2 * GajiPokok2
GajiBersih2 = GajiPokok2 + Tunjangan2 - PPN2
formatGajiPokok2 = f'{GajiPokok2:,.0f}'.replace(',','.')
formatPpn2 = f'{PPN2:,.0f}'.replace(',','.')
formatTunjangan2 = f'{Tunjangan2:,.0f}'.replace(',','.')
formatGajiBersih2 = f'{GajiBersih2:,.0f}'.replace(',','.')

print('-------------------DATA KARYAWAN KETIGA--------------------')
Nama3      = input('Masukan Nama        :')
NIK3       = input('Masukan NIK         :')
GajiPokok3 = float(input('Masukan Gaji Pokok  :Rp.'))
PPN3 = 0.1 * GajiPokok3
Tunjangan3 = 0.2 * GajiPokok3
GajiBersih3 = GajiPokok3 + Tunjangan3 - PPN3
formatGajiPokok3 = f'{GajiPokok3:,.0f}'.replace(',','.')
formatPpn3 = f'{PPN3:,.0f}'.replace(',','.')
formatTunjangan3 = f'{Tunjangan3:,.0f}'.replace(',','.')
formatGajiBersih3 = f'{GajiBersih3:,.0f}'.replace(',','.')

TotalGaji = GajiPokok1 + GajiPokok2 + GajiPokok3
formatTotal = f'{TotalGaji:,.0f}'.replace(',','.')

print('')
print(f'Tahun: {Tahun:<65}  Bulan: {Bulan}')
print('________________________________________________________________________________________________________')
print('|_______________________________________Penghitungan Gaji Karyawan_____________________________________|')
print('|------------------------------------------------------------------------------------------------------|')
print('|    NIK    |    Nama Karyawan   |     Gaji Pokok    |     PPN    |    Tunjangan   |    Gaji Bersih    |')
print('|------------------------------------------------------------------------------------------------------|')
print(f'| {NIK1:<8}  | {Nama1:<17}  |      {formatGajiPokok1:>7}    |  {formatPpn1:>7}  |    {formatTunjangan1:>6}    |     {formatGajiBersih1:>7}    |')
print('|------------------------------------------------------------------------------------------------------|')
print(f'| {NIK2:<8}  | {Nama2:<17}  |      {formatGajiPokok2:>7}    |  {formatPpn2:>7}  |    {formatTunjangan2:>6}    |     {formatGajiBersih2:>7}    |')
print('|------------------------------------------------------------------------------------------------------|')
print(f'| {NIK3:<8}  | {Nama3:<17}  |      {formatGajiPokok3:>7}    |  {formatPpn3:>7}  |    {formatTunjangan3:>6}    |     {formatGajiBersih3:>7}    |')
print('|------------------------------------------------------------------------------------------------------|')
print('|______________________________________________________________________________________________________|')
print('')
print(f'Total Gaji: Rp.{formatTotal}')
