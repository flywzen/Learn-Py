class Player:
    def __init__(self, name, health, ammo):
        self.name = name
        self.health = health
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"{self.name} shoots! Ammo left: {self.ammo}")
        else:
            print(f"{self.name} is out of ammo!")

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
            print(f"{self.type} takes {damage} damage! Health left: {self.health}")
        else:
            print(f"{self.type} is dead!")

player1 = Player("Player1", 100, 10)
enemy1 = Enemy("Zombie", 50)

player1.shoot()
enemy1.take_damage(20)
player1.shoot()
enemy1.take_damage(30)
player1.take_damage(40)
