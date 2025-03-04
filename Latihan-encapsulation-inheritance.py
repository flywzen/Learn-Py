print("Muhammad Rafly Yahya Ramadhan")
print("123140148")
print("PBO RD")

class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}, Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")

    def bergerak(self):
        print("Kendaraan sedang bergerak")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        print(f"Merk: {self.merk}, Jumlah Pintu: {self.jumlah_pintu}")

    def bunyikan_klakson(self):
        print("Peeep! Peeep!")

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga = value

    def info_mobil_sport(self):
        print(f"Mobil Sport {self.merk}, Tenaga Kuda: {self.__tenaga_kuda}, Harga: {self.__harga} juta rupiah")

    def mode_balap(self):
        print("Turbo Mode ON!")

class Kapal(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, tipe, kapasitas):
        super().__init__(jenis, kecepatan_maksimum)
        self.tipe = tipe
        self.kapasitas = kapasitas

    def info_kapal(self):
        print(f"Tipe Kapal: {self.tipe}, Kapasitas: {self.kapasitas} penumpang")

    def berlayar(self):
        print("Aye-aye, Captain!")

class Pesawat(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, maskapai, kapasitas):
        super().__init__(jenis, kecepatan_maksimum)
        self.maskapai = maskapai
        self.kapasitas = kapasitas

    def info_pesawat(self):
        print(f"Maskapai: {self.maskapai}, Kapasitas: {self.kapasitas} penumpang")

    def terbang(self):
        print("On air, sir!")

space = """ """

mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 700, 5000)
mobil_sport.info_kendaraan()
mobil_sport.info_mobil()
mobil_sport.info_mobil_sport()
mobil_sport.bunyikan_klakson()
mobil_sport.mode_balap()

print(space)
kapal = Kapal("Air", 80, "Feri", 500)
kapal.info_kendaraan()
kapal.info_kapal()
kapal.berlayar()

print(space)
pesawat = Pesawat("Udara", 900, "Garuda Indonesia", 250)
pesawat.info_kendaraan()
pesawat.info_pesawat()
pesawat.terbang()
