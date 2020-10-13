import random
import Enemies
import Player
import Combat


def rand():
    room_list = [living_room(), dinning_room(), bedroom(), office(), bathroom()]
    room = room_list[random.randint(0, 4)]
    return room


class entrance:

    def __init__(self):
        weapon_dmg = random.randint(5, 11)
        self.weapon = weapon_dmg

    def start(self):
        Player.intro()
        print("You enter into the old run down building.")
        chance = random.randint(0, 1)
        if chance == 0:
            self.Weapon()
        Player.stats()

    def Weapon(self):
        while True:
            response = input("You see an old rusty pipe on the ground. Do you take it (yes or no)? (attack +" +
                             str(self.weapon) + ") current attack " + str(Player.atk))
            if response == "yes" or response == "no":
                break
            else:
                print("Didn't Catch That")
        if response == "yes":
            Player.atk = self.weapon


class living_room:

    def __init__(self):
        self.ent = Enemies.rand()

    def start(self):
        print("You walk into a room that looks to be an old run down Living Room\nYou see something moving in the dark"
              "\nIt's a ", self.ent.name)
        self.ent.intro()
        while True:
            response = input("Do you choose to fight or try and run past it")
            if response == "fight":
                Combat.fight(self.ent)
                break
            if response == "run":
                Combat.run(self.ent)
                break
            else:
                print("Didn't catch that")


class dinning_room:

    def __init__(self):
        self.ent = Enemies.rand()

    def start(self):
        print("You walk into a room that looks to be an old run down Dinning Room\nYou see something moving in the "
              "dark\nIt's a ", self.ent.name)
        self.ent.intro()
        while True:
            response = input("Do you choose to fight or try and run past it")
            if response == "fight":
                Combat.fight(self.ent)
                break
            if response == "run":
                Combat.run(self.ent)
                break
            else:
                print("Didn't catch that")


class bedroom:

    def __init__(self):
        self.ent = Enemies.rand()

    def start(self):
        print("You walk into a room that looks to be an old run down Bedroom\nYou see something moving in the dark"
              "\nIt's a ", self.ent.name)
        self.ent.intro()
        while True:
            response = input("Do you choose to fight or try and run past it")
            if response == "fight":
                Combat.fight(self.ent)
                break
            if response == "run":
                Combat.run(self.ent)
                break
            else:
                print("Didn't catch that")


class office:

    def __init__(self):
        self.ent = Enemies.rand()

    def start(self):
        print("You walk into a room that looks to be an old run down Office\nYou see something moving in the dark"
              "\nIt's a ", self.ent.name)
        self.ent.intro()
        while True:
            response = input("Do you choose to fight or try and run past it")
            if response == "fight":
                Combat.fight(self.ent)
                break
            if response == "run":
                Combat.run(self.ent)
                break
            else:
                print("Didn't catch that")


class bathroom:

    def __init__(self):
        self.ent = Enemies.rand()

    def start(self):
        print("You walk into a room that looks to be an old run down bathroom\nYou see something moving in the dark"
              "\nIt's a ", self.ent.name)
        self.ent.intro()
        while True:
            response = input("Do you choose to fight or try and run past it")
            if response == "fight":
                Combat.fight(self.ent)
                break
            if response == "run":
                Combat.run(self.ent)
                break
            else:
                print("Didn't catch that")
