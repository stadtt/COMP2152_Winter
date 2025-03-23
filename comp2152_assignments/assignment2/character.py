import random
class Character:


    def __init__(self):

        self.__combat_strength = random.randrange(1, 7)
        self.__health_points = random.randrange(1, 7)

    def __del__(self):
         print("The character is destroyed")

