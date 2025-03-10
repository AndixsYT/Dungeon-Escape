#############################################Initial information###############################################
from time import sleep
import random

# These are the game fight
class Game_fight():
  def FightMechanics(self):
    #Just make the whole fight sequence here and then call to it later
    villainHealth = current_villain.hp
    heroHealth = current_fighter.hp
    while True:
      action = input(f"You chose to fight the {current_villain.name}. Whats your next action\nAttack?\nRun?\n").lower()
      if action == "attack":
        villainHealth = (villainHealth - current_fighter.damage)
        heroHealth = (heroHealth - current_villain.damage)
        print (f"{current_villain.name} has {villainHealth} hp")
        print (f"{current_fighter.name} has {heroHealth} hp")
        break

class fighter():
  def __init__(self, fighter_number, name, hp, damage):
    self.name = name
    self.hp = hp
    self.number = fighter_number
    self.damage = damage

class monster():
  def __init__(self, monster_number, name, hp, damage):
    self.name = name
    self.hp = hp
    self.number = monster_number
    self.damage = damage



#Fighters
normal_man = fighter(1, "Carl", 100, 20)
nyan_cat = fighter(2, "Nyan Cat", 100, 20)
minecraft_steve = fighter(3, "Minecraft steve", 100, 20)
#Enemies
frog = monster(1, "Frog", 30, 1)
worm = monster(2, "Worm", 10, 0.5)
birb = monster(3, "Bird", 27, 7)


#########################################Game Starts here######################################################

print("Welcome to...")
sleep(2)
print("Monster mash!!!\n")
sleep(2)
print("These are the heroes!")
while True:
  Fighter = input(f"1. {normal_man.name}\n2. {nyan_cat.name}\n3. {minecraft_steve.name}\nPick your fighter!\n").lower()

  if Fighter.lower() == "1" or Fighter.lower() == "carl":
    current_fighter = normal_man

  elif Fighter.lower() == "2" or Fighter.lower() == "nyan cat":
    current_fighter = nyan_cat
      
  elif Fighter.lower() == "3" or Fighter.lower() == "minecraft steve" or Fighter.lower() == "steve":
    current_fighter = minecraft_steve
  

  
  #Random villain gets selected
  randomVar = random.randint(1, 100)
  if randomVar <= 33:
    current_villain = frog
  elif randomVar > 66:
    current_villain = birb
  else:
    current_villain = worm

  print("\nVery well")
  sleep(1)
  print(f"You have picked, {current_fighter.name}!\nSTATS: Health:{current_fighter.hp} Damage:{current_fighter.damage}")
  sleep(2)
  print(f"\nYour opponent is {current_villain.name}\nSTATS: Health:{current_villain.hp} Damage:{current_villain.damage}")
  sleep(3)
  print("What would you like to do?")
  sleep(1)
  print("Fight?")
  sleep(1)
  fight_choise = input("Run?\n").lower()


  if fight_choise == "fight":
    Game_fight().FightMechanics()
    playAgain = input("You won the game!\nWould you like to play again?\n").lower()
    if playAgain == ("Yes"):
      Game_fight().FightMechanics()


  elif fight_choise == "run":
    input (f'You chose to fight the "Villain". Whats your next action\n')