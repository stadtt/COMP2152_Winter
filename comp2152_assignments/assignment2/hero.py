from character import Character
import random

class Hero(Character):

    def __init__(self):
        super().__init__()

    def __del__(self):
        print(" The Hero object is being destroyed by the garbage collector")
        super().__del__()

    def hero_attacks(self):
        print("The hero attacks the monster")

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

    def hero_attacks(self,combat_strength, health_points):
        combat_strength = int(combat_strength)
        health_points = int(health_points)
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                   @@@@@@          @@  @    
                @@       @@        @ @@     
               @%         @     @@@ @       
                @        @@     @@@@@     
                   @@@@@        @@       
                   @    @@@@                
              @@@ @@                        
           @@     @                         
       @@*       @                          
       @        @@                          
               @@                                                    
             @   @@@@@@@                    
            @            @                  
          @              @                  

      """
        print(ascii_image)
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(health_points) + ")")
        if combat_strength >= health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(health_points))
        return health_points


