import random
class Character:

    def __init__(self):

        self.combat_strength = random.randrange(1, 7)
        self.health_points = random.randrange(1, 7)

    def __del__(self):
         print("The character is destroyed")
