import random

name = ""
hp = 10
atk = 0
food = 5
candy = 1
bag = [food, candy]
name_bag = ["food", "candy"]
kill = 0
rooms = 0


def intro():
    global name
    name = input("Hello Please Enter Your Name")


def stats():
    print(name + " has " + str(hp) + " HP and +" + str(atk) + " Attack")


def attack():
    hit = (random.randint(10, 15) + atk)
    return hit


def dead():
    if hp <= 0:
        return True
    else:
        return False


def use_bag():
    global candy
    global food
    global hp
    global atk

    print(name_bag[0], name_bag[1])
    print(" ", bag[0], "  ", bag[1])
    while True:
        response = input("Would you like to eat something (yes or no)")
        if response == "yes":
            while True:
                response = input("Would you like to eat candy or snack")
                if response == "candy":
                    if candy == 0:
                        print("You have no candy")
                    else:
                        print("You ate a piece of candy")
                        candy -= 1
                        atk += random.randint(4, 7)
                        stats()
                    break
                if response == "food":
                    if food == 0:
                        print("You have no food")
                    else:
                        print("You ate some food")
                        food -= 1
                        hp += random.randint(5, 10)
                        stats()
                    break
                else:
                    print("Didn't Get That")
            break
        if response == "no":
            break
        else:
            print("Didn't Get That")
