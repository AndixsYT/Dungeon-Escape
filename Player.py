import Game_items

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
    def equips(self):
        self.weapon = [Game_items.fist]