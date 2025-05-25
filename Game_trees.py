import os


###############
###FirstRoom###
###############
knife_picked_up = ("You picked up the knife and put it in you pocket for safe keeping")
initiate = {
    "" : "",
    "[1]: Take another look around" :  {
        "You take another look arround. As your eyes get used to the darkness you notice that in the corner of the dimly lit room, a skeleton holding an old rusty dagger is seated": "",
        "[1]: Pick up the knife" : "room1",
        "[2]: Kick off its head" : "You kicked the head and it flew and shattered against the wall. Congratulations! You are an awful person!"
    },
    "[2]: Inspect the metal bars" : "The metal bars in front of the cell appears to have rusted a long time ago. You should be able to make it through if you hit it with something of equal or greater hardness",
#    "[3]: Try to remember how you got here" : ""
}

###############
####RoomOne####
###############
room1 = {
    "" : "",
    "[1]" : "Hello",
    "[2]" : "Space"
}


###############
##Room_Finder##
###############
all_rooms = {
    "initiate" : initiate,
    "room1" : room1
}