import random

from comp2152_labs.week04.lab04 import combat_strength
from comp2152_labs.week09.main import health_points


class Monster(Character):

    def __init__(self):
        super().__init__(combat_strength,health_points)
        self.__combat_strength = random.randrange(1, 7)
        self.__health_points = random.randrange(1, 7)

    def __del__(self):
        print(" The Monster object is being destroyed by the garbage collector")

    def monster_attacks(self):
        print("The Monster attacks you")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self,value):
        self.__health_points = value

    @property
    def combat_strength(self):
        return self.__m_combat_strength

    @combat_strength.setter
    def combat_strength(self,value):
        self.m_combat_strength = value

    def monster_attacks(m_combat_strength, health_points):
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(monster.combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if monster.combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            health_points -= monster.combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
        return health_points

