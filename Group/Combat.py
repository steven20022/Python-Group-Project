import Enemies
import Player
import random


def stats(ent):
    ent.stats()
    Player.stats()


def fight(ent):
    stats(ent)
    r = random.randint(0, 1)
    if r == 0:
        print(Player.name, " gets to attack first")
        while True:
            options(ent)
            if Enemies.dead(ent.hp):
                break
            stats(ent)
            ent.attack()
            if Player.dead():
                raise NameError("You Died")
            stats(ent)
    else:
        print(ent.name, " gets to attack first")
        while True:
            ent.attack()
            if Player.dead():
                raise NameError("You Died")
            stats(ent)
            options(ent)
            if Enemies.dead(ent.hp):
                break
            stats(ent)


def run(ent):
    print("You try to run past the abomination before you")
    r = random.randint(0, 1)
    if r == 1:
        fight(ent)
    else:
        print("You manage to run past it")


def options(ent):
    while True:
        response = input("Do you attack or check your bag\n(Enter \"attack\" to attack or \" bag\" to check your bag) ")
        if response == "attack":
            ent.hit(Player.attack())
            break
        if response == "bag":
            Player.use_bag()
        else:
            print("Didn't Catch That")
