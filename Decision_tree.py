import os
class Decision_tree_workings:
    def __init__(self, tree):
        while True:
            tmptree = tree.copy()
            print ("What would you like to do?")
            while isinstance(tmptree, dict):
                for key in tmptree:
                    print (key)
                choice = int(input())
                key_choice = list(tmptree)[choice] #Gives keys an index number
                if int(choice) == 0 or choice == "":
                    print (f"{choice} is not a valid choice, please try again")
                else:
                    tmptree = tmptree[key_choice]
            print (tmptree)
            enter = input ("\nPress enter to continue\n")
            if enter == "" or enter == " ":
                os.system("cls")

####### READ THIS: MAKE A LIST OF STEPS/CHOISES TAKEN! EXAMPLE: [1, 2, 3]. STRYK SENAST KANSKE OCH GÅ TILLBAKA.