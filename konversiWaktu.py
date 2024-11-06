#BISMA GYNDARA MAGES JAYALANGIT

waktu = input('masukan hari/jam/menit/detik:')
nilaiWaktu = int(input('masukan nilai waktu:'))

if waktu == 'jam':
    konversiHari = nilaiWaktu / 24
    konversiMenit = nilaiWaktu * 60
    konversiDetik = konversiMenit * 60
    print(f'kedalan hari: {konversiHari:.0f} hari')
    print('kedalam menit:',konversiMenit,'menit')
    print('kedalan detik:',konversiDetik,'detik')
elif waktu == 'menit':
    konversiHari = nilaiWaktu / 1440
    konversiJam = nilaiWaktu / 60
    konversiDetik = nilaiWaktu * 60
    print(f'kedalan hari: {konversiHari:.0f} hari')
    print(f'kedalam jam: {konversiJam:.0f} jam')
    print('kedalam detik:', konversiDetik, 'detik')
elif waktu == 'detik':
    konversiHari = nilaiWaktu / 86400
    konversiMenit = nilaiWaktu / 60
    konversiJam = konversiMenit / 60
    print(f'kedalan hari: {konversiHari:.0f} hari')
    print(f'kedalam jam: {konversiJam:.0f} jam')
    print(f'kedalam menit: {konversiMenit:.0f} menit')
elif waktu == 'hari':
    konversiJam = nilaiWaktu * 24
    konversiMenit = konversiJam * 60
    konversiDetik = konversiMenit * 60
    print(f'kedalam jam: {konversiJam:.0f} jam')
    print(f'kedalam menit: {konversiMenit:.0f} menit')
    print('kedalam detik:', konversiDetik, 'detik')
