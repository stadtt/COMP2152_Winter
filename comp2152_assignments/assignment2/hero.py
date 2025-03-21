from comp2152_assignments.assignment2.main import combat_strength
import random

class Hero:

    def __init__(self):
        small_dice_options = list(range(1, 7))
        self.combat_strength = random.choice(small_dice_options)
        self.health_points = random.choice(small_dice_options)

    def __del__(self):
        print(" The Hero object is being destroyed by the garbage collector")

    def hero_attacks(self):
        print("The hero attacks the monster")

    @property
    def health_points(self):
        return self.health_points

    @health_points.setter
    def health_points(self, value):
        self.health_points = value

    @property
    def combat_strength(self):
        return self.combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self.combat_strength = value