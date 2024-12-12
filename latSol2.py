a = 4
for i in range (a, 1, -1):
    x = a + 2
    b = 1
    for j in range (b, a):
        x = x + b
        b = b + 1
    a = a - 1
print(x)
