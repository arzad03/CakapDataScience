## Soal 1

##Buatlah script “kalkulator” yang terdiri dari dua parameter “x” dan “y” yang akan diisi angka dan parameter “operasi” yang akan diisi nama operasi seperti “penjumlahan”, “pengurangan”, “perkalian” dan “pembagian”
##
##Input:
##kalkulator(a = 10, b = 4, operasi = “penjumlahan”)
##
##Output:
##14

print("Soal 1\n")
def kalkulator(x, y, operasi):
    if operasi == "penjumlahan":
        return x + y
    elif operasi == "pengurangan":
        return x - y
    elif operasi == "perkalian":
        return x * y
    elif operasi == "pembagian":
        if y == 0:
            return "Tidak dapat melakukan pembagian dengan nol"
        return x / y
    else:
        return "Operasi tidak valid"

# Contoh penggunaan
x = 10
y = 4
operasi = "penjumlahan"
hasil = kalkulator(x, y, operasi)

print("Nilai", x, "dilakukan", operasi, "dengan nilai", y, ":", hasil)


## Soal 2

##Buat lah 3 fungsi yang didalamnya terdapat :
##
##* conditional if
##* condition loop
##* args dan kwargs

print("\nSoal 2a\n")
def hitung_rata_rata(*args):
    if len(args) == 0:
        return "Tidak ada nilai yang diberikan"

    total = 0
    for angka in args:
        total += angka

    rata_rata = total / len(args)
    return f"Rata-rata: {rata_rata}"

# Pemanggilan
print(hitung_rata_rata(5, 10, 15))
print(hitung_rata_rata())

print("\nSoal 2b\n")
def daftar_barang(**kwargs):
    if not kwargs:
        return "Tidak ada barang yang diberikan"

    print("Daftar Barang:")
    for nama_barang, harga in kwargs.items():
        print(f"{nama_barang}: Rp{harga}")

# pemanggilan
daftar_barang(beras=12000, gula=15000, minyak=20000)
print(daftar_barang())

print("\nSoal 2c\n")

def terbesar_dan_diskon(*args, **kwargs):
    # Mencari angka terbesar args
    if len(args) == 0:
        terbesar = "Tidak ada angka yang diberikan"
    else:
        terbesar = max(args)

    print(f"Angka terbesar: {terbesar}")

    # diskon harga barang kwargs
    if not kwargs:
        return "Tidak ada barang untuk diskon"

    print("Harga barang setelah diskon:")
    for barang, harga in kwargs.items():
        diskon = harga * 0.1  # Diskon 10%
        harga_diskon = harga - diskon
        print(f"{barang}: Rp{harga_diskon}")

# Pemanggilan
terbesar_dan_diskon(10, 20, 5, beras=12000, gula=15000, minyak=20000)





