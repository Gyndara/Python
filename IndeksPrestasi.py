#BISMA GYNDARA MAGES JAYALANGIT

Nim      = input('Masukan NIM                    :')
Nama     = input('Masukan Nama                   :')
Kelas    = input('Masukan Kelas                  :')
Semester = input('Masukan Semester               :')
Nilai1   = input('Masukan Nilai Matematika 1     :')
Nilai2   = input('Masukan Nilai Algoritma 1      :')
Nilai3   = input('Masukan Nilai Bahasa Indonesia :')

NilaiMat = Nilai1
NilaiAlg = Nilai2
NilaiInd = Nilai3

if Nilai1 == 'A':
   Nilai1 = 4
elif Nilai1 == 'B':
   Nilai1 = 3
elif Nilai1 == 'C':
   Nilai1 = 2
elif Nilai1 == 'D':
   Nilai1 = 1
Bobot1 = Nilai1
Total1 = Nilai1 * 3     

if Nilai2 == 'A':
   Nilai2 = 4
elif Nilai2 == 'B':
   Nilai2 = 3
elif Nilai2 == 'C':
   Nilai2 = 2
elif Nilai2 == 'D':
   Nilai2 = 1   
Bobot2 = Nilai2
Total2 = Nilai2 * 4

if Nilai3 == 'A':
   Nilai3 = 4
elif Nilai3 == 'B':
   Nilai3 = 3
elif Nilai3 == 'C':
   Nilai3 = 2
elif Nilai3 == 'D':
   Nilai3 = 1 
Bobot3 = Nilai3
Total3 = Nilai3 * 2

totalKeseluruhan = Total1 + Total2 + Total3
IndeksPrestasi = totalKeseluruhan / 9

print(f"NIM : {Nim:<30}  Kelas   : {Kelas}")
print(f"Nama: {Nama:<31} Semester: {Semester}")

print('____________________________________________________________')
print('|_____________________INDEKS PRESTASI______________________|')
print('|KODE MK|    NAMA MK   | SKS | NILAI | BOBOT | TOTAL NILAI |')
print('|__________________________________________________________|')
print(f'|01152  | Matematika 1 |  3  |  {NilaiMat}    |   {Bobot1}   |      {Total1}      |')
print('|----------------------------------------------------------|')
print(f'|01153  | Algoritma  1 |  4  |  {NilaiAlg}    |   {Bobot2}   |      {Total2}      |')
print('|----------------------------------------------------------|')
print(f'|01152  | B.Indonesia  |  2  |  {NilaiInd}    |   {Bobot3}   |      {Total3}      |')
print('|__________________________________________________________|')
print(f'Indeks Prestasi: {IndeksPrestasi:.2f}')
