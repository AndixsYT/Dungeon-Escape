import keyboard
from threading import Thread
import Game_rooms
import os

## This is how the program starts running
class Start_menu:
    def __init__(self):
        self.answer = input ("Welcome to Escape The Dungeon\n[1] Start New Game\n[2] How To Play\n")
    def fallout(self):
        true = True
        while true == True:
            if (self.answer) == "1":
                os.system("cls")
                print("You wake up in an seemingly empty cell with walls made of gray-ish stone blocks. It's dark and the only light you can see is coming from a candle located at the other side of the metal bars of which is keeping you locked into the cell.")
                enter = input("Press enter to continue\n")
                if enter == "" or enter == " ":
                    true = False
                    Game_rooms.first_room()
            elif (self.answer) == "2":
                print ("This feature will be implemented later, for now, try playing by guessing your way forward")
                enter = input ("Press enter to continue\n")
                if enter == "" or enter == " ":
                    os.system("cls")
                    self.answer = input ("Welcome to Escape The Dungeon\n[1] Start New Game\n[2] How To Play\n")


## This is the pause menu / inventory
class Pause_menu:
    def __init__(self):
        for i in range(2):
            print ("menu, menu")
def open_menu():
    while True:
        keyboard.wait("escape")
        Pause_menu()
always_pause = Thread(target=open_menu)