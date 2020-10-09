import random
import Player

pk = Player.kill

def rand():
    ent_list = [Zombie(), Skeleton()]
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

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print(self.name, " has " + str(self.hp) + "hp")

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

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print(self.name," has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5)
        Player.hp -= hit

    def hit(self, dmg):
        self.hp -= dmg


