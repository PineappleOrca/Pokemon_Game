# This is a script where I will attempt to learn object oriented programming by creating a pokemon game
from enum import Enum
from menus import display_move_used, display_moveset

class Type(Enum):
    NORMAL = 0
    GRASS = 1
    WATER = 2
    FIRE = 3
    ELECTRIC = 4
    
class Moves:
    def __init__(self, power=0, pp=0, type=Type.NORMAL, accuracy=0):
        self.power = power
        self.pp = pp
        self.type = type
        self.accuracy = accuracy

class Stats(Enum):
    Attack = 0
    Defence = 1
    Speed = 2
    Health = 3

class Status(Enum):
    '''
    Pokemon battle status effects normal,burned,paralyzed,asleep etc
    '''
    Normal = 0
    Burned = 1

class Pokemon:
    # init is used to set values for each square
    def __init__(self,name="", type=Type.NORMAL, stats=[], moveset=[], level=5, doa_status=True, status=Status.Normal):
        self.name = name
        self.type = type
        self.stats = stats 
        self.moveset = moveset 
        self.level = level
        self.doa_status = doa_status    # status of pokemon fainted or alive
        self.status = status            # pokemon status normal/paralyzed/frozen/confused etc

    # This is the getter
    # self is used to refer to an object that we dont possess a name for
    def get_name(self):
        print("Retrieving the name")
        return self.name
    # we put a __ before this private field

    # This is a setter
    def set_name(self, value):
        self.name = value

    # This is the getter
    def get_type(self):
        print("Retrieving the Type")
        return self.type

    # This is the setter
    def set_type(self, value):
        self.type = value 

    # Moveset
    def set_stats(self, value):
        self.stats = value
    
    def get_stats(self):
        return self.stats
    
    # Moveset
    def set_moveset(self, value):
        self.moveset = value
    
    def get_moveset(self):
        return self.moveset

    def fight(self, opponent):
        print(f"What move will {self.name} choose?")
        display_moveset(self)
        # need to add code to ensure the user enters a number between 1 and 4
        user_input = int(input())
        display_move_used(self, user_input)
        # battle calculations
        # RAW attack value v1.0
        # damage formula 
        # Base Damage = (((2L)/5)+2)*(P*A)/(50*D)) + 2 
        # Final Damage = Base Damage x modifier
        # modifier = targets*weather*critical*random*stab*type*burn*others
        damage = self.stats[Stats.Attack.value]
        opponent.stats[Stats.Health.value] -= damage 

    def __str__(self) -> str:
        return "Your Pokemon is: " + self.name + " and it is a " + self.type.name +" type!" 




