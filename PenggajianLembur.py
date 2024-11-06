#{I.S.: Pengguna memasukan lama jam bekerja}
#{F.S.: Menapilkan total gaji yang didapat sesuai jam bekerja}

import os

#badan program
#memasukan lama bekerja
NamaKaryawan = input('MASUKAN NAMA     : ')
LamaBekerja  = int(input('LAMA JAM BEKERJA : '))
os.system('pause')
os.system('cls')
UpahPerjam = 150000

#menghitung total gaji yang didapat selama 40 jam
TotalGaji  = LamaBekerja * UpahPerjam
JamLembur  = 0
GajiLembur = 0

#melakukan penghitungan gaji lembur jika jam bekerja lebih dari 40 jam
if (LamaBekerja > 40):
    JamLembur  = LamaBekerja - 40
    GajiLembur = JamLembur * (UpahPerjam * 2)
    TotalGaji  = 40 * UpahPerjam
    TotalGaji  = TotalGaji + GajiLembur

#menghitung gaji utama tanpa tambahan gaji lembur    
GajiUtama = TotalGaji - GajiLembur

#menampilkan lama bekerja dan total gaji yang didapat
print('  <<<< TOTAL GAJI KARYAWAN >>>>')
print('NAMA KARYAWAN :', NamaKaryawan)
print('LAMA BEKERJA  :', LamaBekerja, ' JAM')
print('LAMA LEMBUR   :', JamLembur, '  JAM')
print(f'GAJI BERSIH   : Rp.{GajiUtama:,.0f}')
print(f'GAJI LEMBUR   : Rp.{GajiLembur:,.0f}')
print(f'TOTAL GAJI    : Rp.{TotalGaji:,.0f}')