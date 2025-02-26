# Muhammad Rafly Yahya Ramadhan
# 123140148
# Tugas 1
# Bintang Piramid

print("                                                                                               ")
print("===============================================================================================")
print("Program untuk membuat segitiga dengan bintang, berdasarkan tinggi baris yang di-input oleh user")
print("===============================================================================================")
print("                                                                                               ")
rows = int(input("-Masukkan jumlah baris: "))

for i in range(0, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
