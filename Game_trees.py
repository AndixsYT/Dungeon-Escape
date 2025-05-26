import os
import Player


knife_pickup = "You picked up the knife and put it in you pocket for safe keeping"
###############
###FirstRoom###  THIS ROOM HAS SUCKED TO MAKE!
###############
initiate2 = {
    "" : "",
    "[1]: Take another look around" :  {
        "You take another look arround. As your eyes get used to the darkness you notice that in the corner of the dimly lit room, a skeleton holding an old rusty dagger is seated": "",
        "[1]: Do nothing" : "",
        "[2]: Kick off its head" : "You kicked the head and it flew and shattered against the wall. Congratulations! You are an awful person!"
    },
    "[2]: Inspect the metal bars" : {
        "The metal bars in front of the cell appears to have rusted a long time ago. You should be able to make it through if you use your dagger" : "",
        "[1]: Use the dagger" : {
            "You use your dagger to strike the rusty metal bars, and with a loud 'thonk', the bar breaks and falls to the ground" : "",
            "[1]: Proceed forward (You wont be able to come back)" : "room1",
            "[2]: Wait" : ""
        },
        "[2]: Do nothing" : ""
    }
}
initiate1 = {
    "" : "",
    "[1]: Take another look around" :  {
        "You take another look arround. As your eyes get used to the darkness you notice that in the corner of the dimly lit room, a skeleton holding an old rusty dagger is seated": "",
        "[1]: Pick up the knife" : "initiate2",
        "[2]: Kick off its head" : "You kicked the head and it flew and shattered against the wall. Congratulations! You are an awful person!\nFrom the darkness you are able to see the head slowly grow back untop his body, creepy!",
    },
    "[2]: Inspect the metal bars" : "The metal bars in front of the cell appears to have rusted a long time ago. You should be able to make it through if you hit it with something of equal or greater hardness",
#    "[3]: Try to remember how you got here" : ""
}


###############
####RoomOne####
###############
room1 = {
    "You have stepped out of the cell and started to walk away. It's not long before you realize that the corridors and rooms are switching places as you move\nAs you turn the corner a slime suddenly shows up in front of you. You already feel your fight or flight instincts kick in\n\nWhat will you do?" : "",
    "[1]: Fight" : "fight",
    "[2]: Escape" : "You cant run away from this"
}


###############
##Room_Finder##
###############
all_rooms = {
    "initiate1" : initiate1,
    "initiate2" : initiate2,
    "room1" : room1
}   