import random
import Player

pk = Player.kill


def rand():
    ent_list = [Zombie(), Skeleton(), Ghost(), Witch(), Vampire(), Werewolf()]
    ent = ent_list[random.randint(0, 5)]
    return ent


def drops():
    weapons = ["Kitchen Knife", "Pocket Knife", "Pipe", "2x4"]
    r = random.randint(0, 3)
    if r == 0:
        print("nothing\n Tough luck")
    if r == 1:
        r = random.randint(1, 2)
        print("some food")
        print("+", r, "food")
        Player.bag[0] += r
    if r == 2:
        random.randint(1, 2)
        print("some candy")
        print("+", r, "candy")
        Player.bag[1] += r
    if r == 3:
        dmg = random.randint(Player.atk, Player.atk + 10)
        wep = random.randint(0, 3)
        print("You find a ", weapons[wep], "That does +", dmg, "Your current weapon damage ",
              Player.atk)
        while True:
            response = input("Do you take it (yes or no)?")
            if response == "yes" or response == "no":
                break
            else:
                print("Didn't Catch That")
        if response == "yes":
            print("You pick up the ", weapons[wep])
            Player.atk = dmg


def dead(hp):
    if hp <= 0:
        Player.kill += 1
        while True:
            response = input("Would you like to check the body for loot (yes or no)")
            if response == "yes":
                print("You walk up to the body and find", end=" ")
                drops()
                break
            if response == "no":
                print("You walk past The dead body")
                break
        return True
    else:
        return False


class Zombie:
    hp = 10
    name = "Zombie"
    id = 0

    def __init__(self):
        self.hp += (random.randint(0, 11)) + (pk * 3)

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print(self.name, " has " + str(self.hp) + "hp")

    def attack(self):
        hit = (random.randint(2, 5)) + (pk * 2)
        Player.hp -= hit
        print(self.name, " hit ", Player.name, " for ", hit, "hp")

    def hit(self, dmg):
        self.hp -= dmg
        print(Player.name, " hit ", self.name, " for ", dmg, "hp")


class Skeleton:
    hp = 10
    name = "Skeleton"

    def __init__(self):
        self.hp += random.randint(0, 11) + (pk * 3)

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print(self.name, " has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5) + (pk * 2)
        Player.hp -= hit
        print(self.name, " hit ", Player.name, " for ", hit, "hp")

    def hit(self, dmg):
        self.hp -= dmg
        print(Player.name, " hit ", self.name, " for ", dmg, "hp")


class Ghost:
    hp = 10
    name = "Ghost"

    def __init__(self):
        self.hp += random.randint(0, 11) + (pk * 3)

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Ghost has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5) + (pk * 2)
        Player.hp -= hit
        print(self.name, " hit ", Player.name, " for ", hit, "hp")

    def hit(self, dmg):
        self.hp -= dmg
        print(Player.name, " hit ", self.name, " for ", dmg, "hp")


class Witch:
    hp = 10
    name = "Witch"

    def __init__(self):
        self.hp += random.randint(0, 11) + (pk * 3)

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Witch has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5) + (pk * 2)
        Player.hp -= hit
        print(self.name, " hit ", Player.name, " for ", hit, "hp")

    def hit(self, dmg):
        self.hp -= dmg
        print(Player.name, " hit ", self.name, " for ", dmg, "hp")


class Vampire:
    hp = 10
    name = "Vampire"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11) + (pk * 3)

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Vampire has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5) + (pk * 2)
        Player.hp -= hit
        print(self.name, " hit ", Player.name, " for ", hit, "hp")

    def hit(self, dmg):
        self.hp -= dmg
        print(Player.name, " hit ", self.name, " for ", dmg, "hp")


class Werewolf:
    hp = 10
    name = "Werewolf"
    id = 1

    def __init__(self):
        self.hp += random.randint(0, 11) + (pk * 3)

    def intro(self):
        print("A " + self.name + " Appears Before You")

    def stats(self):
        print("Werewolf has " + str(self.hp) + "hp")

    def attack(self):
        hit = random.randint(2, 5) + (pk * 2)
        Player.hp -= hit
        print(self.name, " hit ", Player.name, " for ", hit, "hp")

    def hit(self, dmg):
        self.hp -= dmg
        print(Player.name, " hit ", self.name, " for ", dmg, "hp")
