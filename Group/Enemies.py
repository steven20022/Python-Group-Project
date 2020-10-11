import random
import Player

pk = Player.kill

def rand():
    ent_list = [Zombie(), Skeleton(), Ghost(), Witch(), Vampire(), Werewolve()]
    c = -1
    for obj in ent_list:
        c += 1
    ent = ent_list[random.randint(1, c)]
    return ent


class Zombie:
    hp = 10
    name = "Zombie"
    id = 0

    def __init__(self):
        global pk
        self.hp += (random.randint(0, 11)) + (pk * 3)
        name = "Zombie"

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Zombie has " + str(self.hp) + "hp")

    def attack(self):
        hit = (random.randint(2, 5)) + (pk * 2)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg

class Skeleton:
    hp = 10
    name = "Skeleton"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11)
        name = "Skeleton"

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Zombie has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg

class Ghost:
    hp = 10
    name = "Ghost"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11)
        name = "Ghost"

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Ghost has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg


class Witch:
    hp = 10
    name = "Witch"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11)
        name = "Witch"

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Witch has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg

class Vampire:
    hp = 10
    name = "Vampire"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11)
        name = "Vampire"

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Vampire has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg

class Werewolve:
    hp = 10
    name = "Werewolve"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11)
        name = "Werewolve"

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Werewolve has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg