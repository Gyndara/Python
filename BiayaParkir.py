#BISMA GYNDARA MAGES JAYALANGIT

print('       <<<<<< Biaya Parkir >>>>>>>>')
JenisKendaraan = input('Masukan jenis Kendaraan  : ')
NoPol          = input('Masukan No Polisi        : ')

JamMasuk       = input("Masuk  (Jam:Menit)       : ")
JamMasuk, MenitMasuk = JamMasuk.split(':')  
JamMasuk = int(JamMasuk)
MenitMasuk = int(MenitMasuk)

JamKeluar     = input("Keluar (Jam:Menit)       : ")
JamKeluar, MenitKeluar = JamKeluar.split(':')  
JamKeluar = int(JamKeluar)
MenitKeluar = int(MenitKeluar)

if MenitKeluar < MenitMasuk:
    MenitKeluar = MenitKeluar + 60
    JamKeluar = JamKeluar - 1
Menit = MenitKeluar - MenitMasuk 

if JamKeluar < JamMasuk:
    JamKeluar = JamKeluar + 12
Jam = JamKeluar - JamMasuk
print('Lama Parkir              :', Jam, ' Jam ', Menit, ' Menit')

if (Menit > 0):
    Jam = Jam + 1
print('                         :', Jam, ' Jam')

JenisKendaraan = JenisKendaraan.upper()
if JenisKendaraan == 'MOTOR':
    Biaya = 1500 + (Jam - 1) * 500
else:
    Biaya = 3000 + (Jam - 1) * 1000
print('Biaya Parkir             : Rp.', Biaya)
