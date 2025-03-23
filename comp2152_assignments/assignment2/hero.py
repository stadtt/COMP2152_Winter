from comp2152_assignments.assignment2.main import combat_strength
import random

class Hero(Character):

    def __init__(self):
        super().__init__(combat_strength, health_points)
        self.__combat_strength = random.randrange(1, 7)
        self.__health_points = random.randrange(1, 7)

    def __del__(self):
        print(" The Hero object is being destroyed by the garbage collector")

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
        self.combat_strength = value

    def hero_attacks(combat_strength, m_health_points):
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
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(m_health_points))
        return m_health_points