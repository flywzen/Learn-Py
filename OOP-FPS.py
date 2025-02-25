#Muhammad Rafly Yahya Ramadhan
#123140148
#TUGAS WEEK-4 PBO RD

import random as rng

class Player:
    def __init__(self, name, health, ammo, critical_rate):
        self.name = name
        self.health = health
        self.ammo = ammo
        self.initial_ammo = ammo  
        self.critical_rate = critical_rate

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            if rng.random() < self.critical_rate:
                print(f"{self.name} Shoot them dude! yeah, Critical hit! Ammo left : {self.ammo}")
            else:
                print(f"{self.name} Shoot them dude!, Ammo left : {self.ammo}")
        else:
            print(f"{self.name} dude, you just running out of your Ammo! Reload it!")

    def reload(self):
        self.ammo = self.initial_ammo
        print(f"{self.name} has reloaded! Ammo is now {self.ammo}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} takes {damage} damage! Health left: {self.health}")
        else:
            print(f"{self.name} is dead!")

class Enemy:
    def __init__(self, type, health):
        self.type = type
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.type} deal {damage} damage! HP left: {self.health}")
        else:
            print(f"{self.type} is dead, ez win. Noob!")



player1 = Player("Player1", 100, 2, 0.3)  
enemy1 = Enemy("Enemy1", 50)
space = """ """

print(f"Initial ammo {player1.name}: {player1.initial_ammo}")
print(space)
player1.shoot()
enemy1.take_damage(20)
print(space)
player1.shoot()
enemy1.take_damage(30)
print(space)
player1.shoot()
player1.reload()
print(space)
player1.shoot()
enemy1.take_damage(50)
