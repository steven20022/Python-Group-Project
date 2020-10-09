import random
import Enemies
import Player

ent
weapon

def rand():
    room_list = [living_room()]
    c = 0
    for obj in room_list:
        c += 1
    room = room_list[random.randint(1, c)]
    return room


class Enterance:


    def __init__(self):
        weapon_dmg = random.randint(5, 26)
        self.weapon = weapon_dmg

    def start(self):
        Player.intro()
        print("You enter into the old run down building.")
        chance = random.randint(0,1)
        if chance == 0:
            self.Weapon()
        Player.stats()

    def Weapon(self):
        response = input("You see an old rusty pipe on the ground. Do you take it (yes or no)? (attack +" + str(self.weapon) + ") current attack " + str(Player.atk))
        while True:
            if response == "yes" or response == "no":
                break
            else:
                print("Enter a valid room!")
                response = input("You see an old rusty pipe on the ground")
        if response == "yes":
            Player.atk = self.weapon


class living_room:

    global ent
    ent = Enemies.rand()

    def start(self):
        print("You walk into a room that looks to be an old run down Living Room\nYou see something moving in the dark\nIt's a ", self.ent.name)
        self.ent.intro()
        while True:
            response = input("Do you choose to fight or try and run past it")
            if response == "fight":
                break
            if response == "run":
                break
            else:
                print("Didn't catch that")
