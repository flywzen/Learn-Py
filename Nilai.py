#Muhammad Rafly Yahya Ramadhan
#123140148
#Tugas 2

nilai_siswa_dict = {}
jumlah_siswa = int(input("Masukkan jumlah siswa: "))
for i in range(jumlah_siswa):
    print("Masukkan nama siswa ke-", i + 1, ": ", end='')  
    nama_siswa = input()
    print("Masukkan nilai siswa ke-", i + 1, ": ", end='')  
    nilai_siswa = input()

    nilai_siswa_dict[nama_siswa] = nilai_siswa
print("Dictionary nilai siswa:", nilai_siswa_dict)
