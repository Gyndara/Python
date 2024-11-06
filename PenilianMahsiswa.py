a = input("masukan nilai semester 1: ")
b = input("masukan nilai semester 2: ")
c = input("masukan nilai semester 3: ")

d = float(a) 
e = float(b)
f = float(c)
g = (d + e + f) / 3
h = round(g, 2)
print("Nilai rata-rata: ", h)

if h >= 80:
    print("A")
elif h >= 60:
    print("B")
elif h >= 40:
    print("C")
else:
    print("D")