import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)

    def attack(self, opponent):
        opponent.take_damage(20)
        print(f"{self.name} атакует! У {opponent.name} осталось {opponent.health} здоровья.")

def battle(warrior1, warrior2):
    while warrior1.is_alive() and warrior2.is_alive():
        if random.randint(0, 1) == 0:
            warrior1.attack(warrior2)
        else:
            warrior2.attack(warrior1)

    winner = warrior1.name if warrior1.is_alive() else warrior2.name
    print(f"Победитель: {winner}!")


warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

battle(warrior1, warrior2)