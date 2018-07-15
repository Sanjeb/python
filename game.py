from sys import exit
from time import sleep

inventory = []


def game_over(s):
    print(s)
    end = input("do you want to restart y/n")
    if end == "y" or end == "yes":
        start()
    elif end == "n" or end == "no":
        exit(0)

def bathroom():
    print("the tub is filled with blood")
    print("you can 'check' the bath tub")
    print("or you can go 'back' .......")
    a = input()
    while a == "inventory" or a == "inv":
        print(inventory)
        a = input()
    if a == "check":
        bath_tub()
    elif a == "back":
        start()
    else:
        print("you can't go there")


def upstairs():
    print("this room is pretty dusty")
    print("there is nothing here")
    print("you can go back 'down'")
    b = input()
    while b == "inventory" or b == "inv":
        print(inventory)
        b = input()
    if b == "down":
            start()
    else:
        print("you can't go there")



def bath_tub():
    print("your hands are covered with blood")
    print("you find a body bag")
    print("you open it and find a corpse")
    print("you can go 'out' of the bathroom")
    print("you find a 'gun' in the body")
    print("you can pick it up if you want")
    c = input()
    while c == "gun":
        inventory.append("gun")
        c = input()
    while c == "inventory" or c == "inv":
        print(inventory)
        c = input()
    if c == "out":
        start()
    else:
        print("you can't go there")


def living_room():
    print("NEIGHBOUR: take a seat")
    sleep(1)
    print("YOU: madam, you have been suspected for a murder across the house")
    print("type 'c' to continue")
    cont = input()
    while cont != "c":
        cont = input(">")
    print("NEIGHBOUR: I don't think it's right for you to")
    print("           suspect me")
    print("           I live here all alone ")
    print("           all I get is my husband's")
    print("           pension. why do you think I did it ?")
    print("type 'c' to continue")
    cont = input()
    while cont != "c":
        cont = input(">")
    print("YOU: that is classified")
    print("     but I think that is")
    print("     for now")
    sleep(4)


def out():
    print("you can 'ring' the bell")
    f = input()
    while f != "ring":
        f = input()
    print("you have rung the bell")
    sleep(5)
    print("there is no one answering. you can 'ring' the bell again")
    f = input()
    while f != "ring":
        f = input()
    print("NEIGHBOUR: Coming!!!")
    sleep(1.5)
    print("neighbour opens the door")
    print("NEIGHBOUR: How may I help you ?")
    print("type 'c' to continue")
    cont = input()
    while cont != "c":
        cont = input(">")
    print("YOU: I'am with the FBI.")
    print("NEIGHBOUR: Why are you here ? what happened")
    print("YOU: Can we talk about it inside")
    print("type 'c' to continue")
    cont = input()
    while cont != "c":
        cont = input(">")
    print("NEIGHBOUR: sure, come in")
    living_room()


def neighbour():
    print("                                   ")
    print("-----------------------------------")
    print("           chapter - 2             ")
    print("                                   ")
    print("you are in the neighbours house now")
    print("you can 'interrogate' the person in the house")
    e = input()
    while e != "interrogate":
        e = input()
    out()


def well():
    print("you find a pathway which leads to ")
    print("the neighbours home. You have discovered that")
    print("someone from the neighbours home has done the murder")
    sleep(2)
    neighbour()


def garden():
    print("you are in the garden.")
    print("it has beautiful flowers and insects")
    print("buzzing around")
    print("you can go 'down' the well")
    print("you can also go back 'in'")
    d = input()
    while d == "inventory" or d == "inv":
        print(inventory)
        d = input()
    if d == "in":
        start()
    elif d == "down":
        well()
    elif d == "inventory":
        print(inventory)
        garden()
    else:
        print("you can't go there")



def intro():
    print ()
    print("welcome, to Detective mystery")
    print("your mission is to find what has")
    print("happened here and who did it")
    print("----------------------------------------------")
    print("you are in a house. there is blood everywhere")
    print("you can also use the inventory")


def start():
    print("You can go 'up' the stairs, 'outside' to the back yard")
    print("or to the bathroom which is in the 'east' ")
    test = input()
    if test == "outside":
        if "gun" in inventory:
            print("the door is chained with a lock")
            print("use your gun to break the lock")
            print("type 'shoot'")
            test = input()
            while test != "shoot":
                test = input()
            print("kaboom !!!!!")
            sleep(1)
            print("you are in the garden")
            print("                     ")
            garden()
        else:
            print("that door is chained with a lock")
            print("you can't go there")
            test = input(">")
    if test == "up":
        upstairs()
    elif test == "east":
        bathroom()
    elif test == "inventory":
        print(inventory)
        start()
    else:
        print("you can't go there")


intro()
start()
