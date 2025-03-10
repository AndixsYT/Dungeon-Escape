###############
##ShowActions##
###############
class RoomActions:
    def __init__(self, choice):
        self.choice = choice

    def fallout(self):
        for i in self.choice:
            print(i)
        


###############
#RoomTemplates#
###############
# class First_room(RoomActions):
#     def __init__(self, choice):
#         super().__init__(choice)