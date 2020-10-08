# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Enemies
import Player
import Rooms
import os
import time


def clear():
    # for windows
    os.system('cls')
    os.system("ls")
    time.sleep(2)


if __name__ == '__main__':
    e = Rooms.enterance()
    l = Rooms.living_room()
    e.start()
    l.start()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
