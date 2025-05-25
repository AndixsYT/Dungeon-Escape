from time import sleep
from Game_menu import Start_menu
import Game_menu
import os
from Player import Player

###############
#####Story#####
###############
#Game_menu.always_pause.start()

the_player = Player(hp=50, inventory=Player.invent, weapon=Player.equips, name="player")
os.system("cls")
Start_menu().fallout()