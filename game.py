from sys import exit
from time import sleep


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
    if b == "down":
        start()
    else:
        print("you can't go there")




def bath_tub():
    print("your hands are covered with blood")
    print("you find a body bag")
    print("you open it and find a corpse")
    print("you can go 'out' of the bathroom")
    c = input()
    if c == "out":
        start()
    else:
        print("you can't go there")


def well():
    print("you find a pathway which leads to ")
    print("the neighbours home. You have discovered")
    print("someone from the neighbours home")
    sleep(1)
    game_over("you have won the beta game. please wait for the alpha release")




def garden():
    print("you are in the garden.")
    print("it has beautiful flowers and insects")
    print("buzzing around")
    print("you can go 'down' the well")
    print("you can also go back 'in'")
    d = input()
    if d == "in":
        start()
    elif d == "down":
        well()
    else:
        print("you can't go there")


def intro():
    print ()
    print("welcome, to Detective mystery")
    print("your mission is to find what has")
    print("happened here and who did it")
    print("----------------------------------------------")
def start():
    print("you are in a house. there is blood everywhere")
    print("You can go 'up' the stairs, 'outside' to the back yard")
    print("or to the bathroom which is in the 'east' ")
    test = input()
    if test == "up":
        upstairs()
    elif test == "outside":
        garden()
    elif test == "east":
        bathroom()
    else:
        print("you can't go there")


intro()
start()
