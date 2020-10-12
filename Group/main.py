# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Enemies
import Player
import random
import Rooms
import os


def rand_room():
    rooms = [Rooms.living_room]
    r = random.randint(0, 0)
    return rooms[r]


def start():
    Rooms.enterance.start()
    while True:
        room = rand_room()
        room.start()


def clear():
    # for windows
    os.system('cls')
    os.system("ls")


if __name__ == '__main__':
    e = Rooms.enterance()
    l = Rooms.living_room()
    e.start()
    clear()
    l.start()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
