import random as rng
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self._name = name  
        self._health = health

    @property
    def name(self):  
        return self._name

    @property
    def health(self):
        return self._health

    @abstractmethod
    def take_damage(self, damage):  
        pass

class Player(Character):
    def __init__(self, name, health, ammo, critical_rate):
        super().__init__(name, health)
        self._ammo = ammo  
        self._initial_ammo = ammo
        self._critical_rate = critical_rate

    @property
    def ammo(self):
        return self._ammo

    @property
    def initial_ammo(self):
        return self._initial_ammo

    def shoot(self):
        if self._ammo > 0:
            self._ammo -= 1
            critical = rng.random() < self._critical_rate
            if critical:
                print(f"{self.name} Shoot them dude! Critical hit! Ammo left: {self._ammo}")
                return 30  
            else:
                print(f"{self.name} Shoot them dude! Ammo left: {self._ammo}")
                return 20  
            
        else:
            print(f"{self.name} out of ammo! Reload!")
            return 0

    def reload(self):
        self._ammo = self._initial_ammo
        print(f"{self.name} reloaded! Ammo: {self._ammo}")

    
    def take_damage(self, damage):
        self._health -= damage
        if self._health > 0:
            print(f"{self.name} takes {damage} damage! Health: {self._health}")
        else:
            print(f"{self.name} is dead!")


class Enemy(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def take_damage(self, damage):
        self._health -= damage
        if self._health > 0:
            print(f"{self.name} takes {damage} damage! HP left: {self._health}")
        else:
            print(f"{self.name} defeated!")

player1 = Player("Player1", 100, 2, 0.3)
enemy1 = Enemy("Enemy1", 50)
space = " "

print(f"Initial ammo: {player1.initial_ammo}")
print(space)

dmg = player1.shoot()
if dmg > 0:
    enemy1.take_damage(dmg)
print(space)

dmg = player1.shoot()
if dmg > 0:
    enemy1.take_damage(dmg)
print(space)

dmg = player1.shoot()
if dmg > 0:
    enemy1.take_damage(dmg)
else:
    print("No damage dealt")
print(space)

player1.reload()
print(space)

dmg = player1.shoot()
if dmg > 0:
    enemy1.take_damage(dmg)
