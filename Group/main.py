# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Player
import Rooms
import os


def start():
    Rooms.entrance().start()
    while True:
        room = Rooms.rand()
        room.start()
        Player.rooms += 1


def clear():
    # for windows
    os.system('cls')
    os.system("ls")


def gameover():
    print("Game Over\nYou killed", Player.kill, "Enemies\nYou Beat", Player.rooms, "rooms")


if __name__ == '__main__':
    try:
        start()
    except NameError:
        gameover()
