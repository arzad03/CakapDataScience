## Soal 1
print("Soal 1")
max_stars = int(input("Masukkan tinggi sergitiga : "))

# Mencetak kenaikan bintang
for i in range(1, max_stars + 1):
    print('* ' * i)

#### Soal 2

print("\nSoal 2")

# Nilai kenaikan bintang
max_stars = 5

# Kenaikan bintang
for i in range(1, max_stars + 1):
    print('* ' * i)

# Penurunan bintang 
for i in range(max_stars - 1, 0, -1):
    print('* ' * i)

## Soal 3
## a. Buat contoh while yang di dalamnya terdapat if-elif-else

print("\nSoal 3a. Membuat contoh while dengan if-elif-else")

angka = int(input("Masukkan angka 1-10 : " ))

while angka <= 10:
  if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
  elif angka % 3 == 0:
    print(f"{angka} adalah bilangan kelipatan 3")
  else:
    print(f"{angka} adalah bilangan ganjil dan bukan kelipatan 3")
  angka += 1

## b. Buat contoh nested loop yang di dalamnya terdapat if-else

print("\nSoal 3b. Membuat nested loop dengan if-else")

num_first = int(input("Masukkan nilai awal : "))
num_end = int(input("Masukkan nilai akhir : "))

for i in range(num_first, num_end):  
    for j in range(num_first, num_end):  
        if i == j:  
            print(f"i = {i}, j = {j} -> i dan j sama")
        else:  # Kondisi else
            print(f"i = {i}, j = {j} -> i dan j berbeda")

