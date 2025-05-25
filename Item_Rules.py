###############
###Item_Base###
###############
class Consumables:
    def __init__(self, type, item_name, effect, uses, duration, weight, worth, price, info):
        self.type = type
        self.item_name = item_name
        self.effect = effect
        self.uses = uses
        self.duration = duration
        self.weight = weight
        self.worth = worth
        self.price = price
        self.info = info 


###############
###Equipment###
###############
class Armor():
    def __init__(self, type, item_name, defense, weight, worth, price, info):
        self.defense = defense
        self.type = type
        self.item_name = item_name
        self.weight = weight
        self.worth = worth
        self.price = price
        self.info = info

class Weapon():
    def __init__(self, type, item_name, damage, uses, weight, worth, price, info):
        self.damage = damage
        self.type = type
        self.item_name = item_name
        self.uses = uses
        self.weight = weight
        self.worth = worth
        self.price = price
        self.info = info


###############
###GameItems###
###############
class Potions(Consumables):
    pass

class Quest_Items():
    def __init__(self):
        pass

