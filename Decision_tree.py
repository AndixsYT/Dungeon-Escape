import os
import Player
import Game_rooms
import Game_trees
class Decision_tree_workings:
    def __init__(self, tree):
        while True:
            tmptree = tree.copy()
            print ("What would you like to do?")
            while isinstance(tmptree, dict):
                try:
                    for key in tmptree:
                        print (key)
                    choice = int(input())
                    if 1 <= choice < len(tmptree): #Checks if what you typed is a number withing the range of the number of keys found in the dictionary
                        os.system("cls")
                        key_choice = list(tmptree)[choice] #Gives keys an index number making me able to pick pick a value by number                    
                        tmptree = tmptree[key_choice] #Enters the dictionary chosen
                    else:
                        print (f"{choice} is not a valid choice, please try again")
                except:
                    print (f"What you just typed is not a valid choice, please try again")
            if tmptree in Game_trees.all_rooms: #This checks if the value of the dict matches with the names of other rooms and then switches to that room
                tree = Game_trees.all_rooms[tmptree]
            elif tmptree == "fight":
                Player.fight().FightMechanics()
            elif enter != "THE ENTIRE BEE MOVIE SCRIPT":
                os.system("cls")

            else:    
                print (tmptree) #prints the most utter leaf
            enter = input ("\nPress enter to continue\n")

####### READ THIS: MAKE A LIST OF STEPS/CHOISES TAKEN! EXAMPLE: [1, 2, 3]. STRYK SENAST KANSKE OCH GÅ TILLBAKA.  FÖR SENARE