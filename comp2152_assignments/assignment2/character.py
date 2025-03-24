import random
class Character:


    def __init__(self):

        self.__combat_strength = random.randrange(1, 7)
        self.__health_points = random.randrange(1, 7)

    def __del__(self):
         print("The character is destroyed")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        self.__health_points = value

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self.__combat_strength = value
