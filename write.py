#Muhammad Rafly Yahya Ramadhan
#123140148
#Tugas 3

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
quote = input("Masukkan Motto hidupmu: ")
resolusi = input("Masukkan Resolusi di Tahun ini: ")

with open("AboutMe.txt", "w") as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi: {resolusi}\n")

print("File AboutMe.txt telah berhasil dibuat!")
print("Goodluck!", nama)
