from PIL import Image

# Membuka gambar dan mengubah ukurannya
img = Image.open("image2.jpg")
img = img.resize((80, 40))  # Ubah ukuran agar muat di terminal
img = img.convert("L")  # Ubah gambar ke skala abu-abu (grayscale)

# Karakter ASCII untuk intensitas warna
ascii_chars = "@%#*+=-:. "

# Mengonversi piksel menjadi karakter ASCII
def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 32]
    return ascii_str

# Menampilkan gambar dalam format ASCII
ascii_str = pixel_to_ascii(img)
width = img.width
ascii_img = "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])
print(ascii_img)
