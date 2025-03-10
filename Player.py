###############
###User_info###
###############
class Player:
    def __init__(self, inventory, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = inventory
    def invent(self):
        self.inventory = [[],[],[],[]]