import random


class Monster:

    def __init__(self):

        self.m_combat_strength = random.randrange(1, 7)
        self.m_health_points = random.randrange(1, 7)

    def __del__(self):
        print(" The Monster object is being destroyed by the garbage collector")

    def monster_attacks(self):
        print("The Monster attacks you")

    @property
    def health_points(self):
        return self.health_points

    @health_points.setter
    def health_points(self,value):
        self.health_points = value

    @property
    def combat_strength(self):
        return self.m_combat_strength

    @combat_strength.setter
    def combat_strength(self,value):
        self.m_combat_strength = value
