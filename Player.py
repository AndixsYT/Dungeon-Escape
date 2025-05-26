import Game_items
from time import sleep
###############
###User_info###
###############
class Player:
    def __init__(self, inventory, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.inventory = inventory
    def invent(self):
        self.inventory = [[],[],[],[]]

the_player = Player(hp=50, inventory=Player.invent, weapon=Game_items.fist, name="player")

###############
####Monster####
###############
class Monster:
    def __init__(self, hp, attack, type):
        self.hp = hp
        self.attack = attack
        self.type = type

###############
###Monsters####
###############
slime = Monster(10, 2, "Slime")


###############
#FightSequence#  HIGHLY EXPERIMENTAL
###############
class fight():
    def FightMechanics(self):
        monsterHP = slime.hp
        playerHP = the_player.hp
        while True:
            if not monsterHP <= 0: 
                action = input(f"You chose to fight the {slime.type}. Whats your next action\nAttack?\n").lower()
                if action == "attack" or action == "1":
                    monsterHP = (monsterHP - the_player.weapon.damage)
                    playerHP = (playerHP - slime.attack)
                    if monsterHP <0:
                        monsterHP = 0
                        print (f"{slime.type} have {monsterHP} hp")
                        print (f"You Have {playerHP} hp")
                    else:
                        print (f"{slime.type} have {monsterHP} hp")
                        print (f"You Have {playerHP} hp")
                else:
                    print("That was not a valid choice. Try again")
            else:
                print ("You win the game. This is as far as I have gotting with this, but it wouldnt be too difficult to add more rooms and enemies.\nWell played and all that.")
                sleep(5)
                exit()