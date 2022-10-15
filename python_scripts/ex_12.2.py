import random

class Coin:

    def __init__(self):
        self.__side_up = "Heads"
        self.toss()

    def toss(self):
        if random.randint(0,1) == 0:
            self.__side_up = "Tails"
        else:
            self.__side_up = "Heads"

    def get_side_up(self):
        return self.__side_up

    def set_side_up(self, face):
        if face == "Heads" or face == "Tails":
            self.__side_up = face
        else:
            print("Invalid face")


coin1 = Coin()
coin1.set_side_up("Heads")
print(coin1.get_side_up())
coin1.set_side_up("No face")

# for i in range(20):
#     coin1.toss()
#     print(coin1.side_up)