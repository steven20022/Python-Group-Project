import random

name = ""
hp = 100
atk = 0
food = 0
candy = 0
bag = [food, candy]
kill = 0

def intro():
    global name
    name = input("Hello PLease Enter Your Name")


def stats():
    print(name + " has " + str(hp) + " HP and +" + str(atk) + " Attack")


def attack(ent_hp):
    hit = (random.randint(10, 15) + atk)
    ent_hp = ent_hp - hit


