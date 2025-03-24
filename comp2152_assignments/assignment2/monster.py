import random
from character import Character


class Monster(Character):

    def __init__(self):
        super().__init__()

    def __del__(self):
        print(" The Monster object is being destroyed by the garbage collector")
        super().__del__()

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
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self,value):
        self.__combat_strength = value

    def monster_attacks(self,combat_strength, health_points):
        combat_strength = int(combat_strength)
        health_points = int(health_points)
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
        print("    |    Monster's Claw (" + str(combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            health_points -= combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
        return health_points

