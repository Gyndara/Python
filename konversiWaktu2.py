#BISMA GYNDARA MAGES JAYALANGIT

NilaiDetik = int(input('Masukan Nilai Detik'))

hari = NilaiDetik // (24 * 3600)
NilaiDetik = NilaiDetik % (24 * 3600)
jam = NilaiDetik // 3600
NilaiDetik = NilaiDetik % 3600
menit = NilaiDetik // 60
detik = NilaiDetik % 60

print('Jumlah :', hari, ' hari')
print('Jumlah :', jam, ' jam')
print('Jumlah :', menit, ' menit')
print('Jumlah :', detik, ' detik')
