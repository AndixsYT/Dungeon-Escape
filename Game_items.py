from Item_Rules import Armor, Weapon, Potions

###############
#####Armor#####
###############
#       Template = Armor(type, item name, defense, weight, worth, price, info)
tattered_clothes = Armor("armor", "Tattered Clothes", 0, 2, 5, 0, "These are the clothes you woke up in. Not much left of them at this point.")



###############
####Weapons####
###############
#   Template = Weapon(type, item name, damage, uses, weight, worth, price, info)
fist = Weapon("weapon", "Fists", 4, 0, -1, 0, 0, "Thir are yer ain bloody fists! They've been wi ye fur yer whole life an' hae never let ye doon so far!")
rusty_dagger = Weapon("weapon", "Rusty Dagger", 8, 1, 15, 7, 10, "This is an old metal dagger. It has now completely rusted and won't hold for much longer, but you can tell that it got plenty of use by whomever was its previous owener.")
sturdy_stick = Weapon("weapon", "Sturdy Stick", 5, 0.1, 20, 2, 3, "This is probably the most sturdy stick you've ever seen, but don't let that fool you. This stick will still break eventually")


###############
####Potions####
###############
#     Template = Potions(type, item_name, effect, uses, duration, weight, worth, price, info)
small_h_potion = Potions("potion", "Small Health Potion", "healing", 0, "duration", 0.7, 3, 5, "This is a small healing potion. After use you will regain 20 health.")

###############
##Quest_items##
###############