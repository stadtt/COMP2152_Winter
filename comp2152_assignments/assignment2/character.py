import random
class Character:

    def __init__(self):
        small_dice_options = list(range(1, 7))
        self.combat_strength = random.choice(small_dice_options)
        self.health_points = random.choice(small_dice_options)

    def __del__(self):
        