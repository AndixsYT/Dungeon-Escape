###############
###Item_Base###
###############
class Equipment:
    def __init__(self, type, item_name, uses, weight, worth, price, info):
        self.type = type
        self.item_name = item_name
        self.uses = uses
        self.weight = weight
        self.worth = worth
        self.price = price
        self.info = info

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
class Armor(Equipment):
    def __init__(self, type, item_name, defense, weight, worth, price, info):
        super().__init__(type, item_name, weight, worth, price, info)
        self.defense = defense

class Weapon(Equipment):
    def __init__(self, type, item_name, damage, uses, weight, worth, price, info):
        super().__init__(type, item_name, uses, weight, worth, price, info)
        self.damage = damage


###############
###GameItems###
###############
class Potions(Consumables):
    pass

class Quest_Items():
    def __init__(self):
        pass

