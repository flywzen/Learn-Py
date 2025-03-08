import random

class Fighter:
    def __init__(self, name, hp, attack, accuracy=0.8):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.accuracy = accuracy  # Opsional: kemungkinan serangan kena

    def is_attack_hit(self):
        return random.random() < self.accuracy

class Game:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.round = 1

    def start(self):
        while True:
            print(f"\n--- Round {self.round} ---")
            self.display_status()
            
            # Pemilihan aksi untuk fighter1
            action1 = self.get_action(self.fighter1)
            if action1 == 3:
                print(f"{self.fighter1.name} menyerah!")
                break
            
            # Pemilihan aksi untuk fighter2
            action2 = self.get_action(self.fighter2)
            if action2 == 3:
                print(f"{self.fighter2.name} menyerah!")
                break
            
            # Proses aksi
            self.process_actions(action1, action2)
            
            # Cek apakah ada fighter yang HP-nya habis
            if self.fighter1.hp <= 0 or self.fighter2.hp <= 0:
                break
            
            self.round += 1
        
        # Tentukan pemenang
        winner = None
        if self.fighter1.hp <= 0 and self.fighter2.hp <= 0:
            print("Kedua fighter hancur!")
        elif self.fighter1.hp <= 0:
            winner = self.fighter2
        elif self.fighter2.hp <= 0:
            winner = self.fighter1
        
        if winner:
            print(f"{winner.name} menang!")

    def get_action(self, fighter):
        while True:
            try:
                print("1. Attack    2. Defense    3. Retreat")
                choice = int(input(f"{fighter.name}, pilih aksi: "))
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Pilihan tidak valid. Masukkan 1-3.")
            except ValueError:
                print("Masukkan angka yang valid.")

    def display_status(self):
        print(f"### {self.fighter1.name} [{self.fighter1.hp}|{self.fighter1.attack}]")
        print(f"### {self.fighter2.name} [{self.fighter2.hp}|{self.fighter2.attack}]")

    def process_actions(self, action1, action2):
        damage_to_fighter2 = 0
        damage_to_fighter1 = 0
        
        # Fighter1 menyerang
        if action1 == 1:
            if self.fighter1.is_attack_hit():
                damage = self.fighter1.attack
                if action2 == 2:  # Fighter2 bertahan
                    damage = int(damage * 0.5)
                damage_to_fighter2 = damage
                print(f"{self.fighter1.name} menyerang {self.fighter2.name} dan memberikan {damage} damage!")
            else:
                print(f"{self.fighter1.name} menyerang, tetapi meleset!")
        
        # Fighter2 menyerang
        if action2 == 1:
            if self.fighter2.is_attack_hit():
                damage = self.fighter2.attack
                if action1 == 2:  # Fighter1 bertahan
                    damage = int(damage * 0.5)
                damage_to_fighter1 = damage
                print(f"{self.fighter2.name} menyerang {self.fighter1.name} dan memberikan {damage} damage!")
            else:
                print(f"{self.fighter2.name} menyerang, tetapi meleset!")
        
        # Update HP
        self.fighter1.hp -= damage_to_fighter1
        self.fighter2.hp -= damage_to_fighter2
        
        # Pastikan HP tidak negatif
        self.fighter1.hp = max(self.fighter1.hp, 0)
        self.fighter2.hp = max(self.fighter2.hp, 0)
        
        # Tampilkan status HP setelah serangan
        print(f"\n{self.fighter1.name} HP: {self.fighter1.hp}")
        print(f"{self.fighter2.name} HP: {self.fighter2.hp}")

# Inisialisasi fighter dan mulai permainan
fighter1 = Fighter("Jonggun", 500, 10)
fighter2 = Fighter("Yohan", 750, 8)
game = Game(fighter1, fighter2)
game.start()
