# Buat contoh :

# numpy array (1D, 2D, 3D)
# numpy join
# numpy split
# operasi matrik

import numpy as np

print("SOal 1\n")

# Numpy Array (1D, 2D, 3D)
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", arr_1d)
print("arr_id berdimensi : ", arr_1d.ndim)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr_2d)
print("arr_id berdimensi : ", arr_2d.ndim)

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3D Array:\n", arr_3d)
print("arr_id berdimensi : ", arr_3d.ndim)

# Numpy Join
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Concatenate
arr_concat = np.concatenate((arr1, arr2))
print("\nConcatenated Array:\n", arr_concat)

# Numpy Split
arr_split = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr_split, 3)
print("\nSplit Array:\n", new_arr)

# Operasi Matriks
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Penjumlahan matriks
result_add = matrix_a + matrix_b
print("\nPenjumlahan Matriks:\n", result_add)

# Pengurangan matriks
result_min = matrix_a - matrix_b
print("\nPengurangan Matriks:\n", result_min)

# Perkalian matriks
result_multiply = np.dot(matrix_a, matrix_b)
print("\nPerkalian Matriks:\n", result_multiply)

# Pangkat dengan power
result_power = np.power(matrix_a, 3)
print("\nPerpangkatan 3 Matriks a :\n", result_power)

# Perhitungan sin
result_sin = np.sin(matrix_a)
print("\nSin Matriks a :\n", result_sin)

# Soal 2
# Buatlah numpy array dengan matrik ukuran 3x4 dan range array 10-30
# Kemudian lakukan flatten
# cari nilai statistik (mean, median, dsb)

print("\nS0al 2\n")

# numpy array dengan range 10-30 dan reshape menjadi matriks 3x4
arr = np.arange(10, 22).reshape(3, 4)

# Melakukan flatten pada array
arr_flat = arr.flatten()

# Mencari nilai statistik
mean = np.mean(arr_flat)
median = np.median(arr_flat)
std_dev = np.std(arr_flat)
var = np.var(arr_flat)
max_val = np.max(arr_flat)
min_val = np.min(arr_flat)
q1 = np.percentile(arr_flat, 25)
q3 = np.percentile(arr_1d, 75)
iqr = q3 - q1

# Menampilkan hasil
print("Array Awal:\n", arr)
print("\nArray Setelah Flatten:\n", arr_flat)
print("\nNilai Statistik:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standar Deviasi: {std_dev}")
print(f"Variansi: {var}")
print(f"Nilai Maksimum: {max_val}")
print(f"Nilai Minimum: {min_val}")
print("Kuartil Pertama (Q1):", q1)
print("Kuartil Ketiga (Q3):", q3)
print("Rentang Interkuartil (IQR):", iqr)
