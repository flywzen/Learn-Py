from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, warna, harpa):
        self.warna = warna
        self.harpa = harpa  
    
    @abstractmethod
    def maju(self):
        pass
    
    @abstractmethod
    def berhenti(self):
        pass
    
    @abstractmethod
    def ngebut(self):
        pass
    
    def klakson(self):
        print("Telolet! Telolet!")

class Mobil(Kendaraan):
    def maju(self):
        print(f"Mobil {self.warna} bergerak maju")
    
    def berhenti(self):
        print(f"Mobil {self.warna} berhenti mendadak")
    
    def ngebut(self):
        print(f"Mobil {self.warna} ngebut dengan kecepatan 120km/jam!")

class Truk(Kendaraan):
    def maju(self):
        print(f"Truk {self.warna} bergerak perlahan")
    
    def berhenti(self):
        print(f"Truk {self.warna} mengerem berbunyi KREEET")
    
    def ngebut(self):
        print(f"Truk {self.warna} maksimal ngebut 80km/jam")

class Sopedalkotor(Kendaraan):
    def maju(self):
        print(f"Sopedalkotor {self.warna} melaju zig-zag")
    
    def berhenti(self):
        print(f"Sopedalkotor {self.warna} berhenti sambil ngepot")
    
    def ngebut(self):
        print(f"Sopedalkotor {self.warna} ngebut 100km/jam")


mobil_merah = Mobil("Merah", 250_000_000)
truk_biru = Truk("Biru", 500_000_000)
motor_hijau = Sopedalkotor("Hijau", 20_000_000)

mobil_merah.maju()
mobil_merah.ngebut()
mobil_merah.klakson()

truk_biru.berhenti()

motor_hijau.maju()
motor_hijau.klakson()
