panjang = float(input('panjang:'))
lebar   = float(input('lebar:'))
tinggi  = float(input('tinggi:'))
konversi = 2.54

konversiPanjang = panjang * konversi
konversiLebar   = lebar * konversi
konversiTinggi  = tinggi * konversi

volumeBalok = konversiPanjang * konversiLebar * konversiTinggi

print(f'volume balok: {volumeBalok:.2f} cm3')



