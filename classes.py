# This is a script where I will attempt to learn object oriented programming by creating a pokemon game
from enum import Enum
from menus import display_move_used, display_moveset
import json
import random
from dataclasses import dataclass, field

class Type(Enum):
    NORMAL = 0
    GRASS = 1
    WATER = 2
    FIRE = 3
    ELECTRIC = 4
    STEEL = 5

@dataclass
class Moves:
    name: str = ""
    power: int = 0
    pp: int = 0
    type: Type = Type.NORMAL
    accuracy: int = 0

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

@dataclass
class Pokemon:
    name: str = ""
    type: Type = Type.NORMAL
    stats: list[int] = field(default_factory=list)
    moveset: list[str] = field(default_factory=list)
    level: int = 5
    doa_status: bool = True
    status: Status = Status.Normal

    def fight(self, opponent):
        # need to add code to ensure the user enters a number between 1 and 4
        display_moveset(self)
        user_input = input(f"What move will {self.name} choose?  ")
        if not user_input:
            print(f"Error: You must pick a move (1-4) for {self.name} to use!")        
        try:
            value = int(user_input)
        except ValueError:
            print("Error: Please enter a number between 1 and 4.")
        if value < 1 or value > 4:
            print("Error: Please pick a number between 1 and 4")
        self.use_move(int(user_input)-1, opponent)

    def ai_fight(self, opponent):
        print(f"Seto Kaiba is thinking.......")
        self.use_move(random.randint(0,3), opponent)

    def get_damage(self, move, opponent):
        base_damage = ((2.0*self.level/5)+2)*((move.power*self.stats[Stats.Attack.value])/(50*opponent.stats[Stats.Defence.value])) + 2
        stab = self.get_stab_factor(move)
        type_effectiveness = self.get_type_effectiveness(move, opponent)
        if(type_effectiveness > 1.0):
            print("Its super effective!!!")
        elif(type_effectiveness < 1.0):
            print("Its not very effective......")
        else:
            print("BOOM what a move!")
        damage = int(base_damage*stab*type_effectiveness)
        return damage
    
    def get_stab_factor(self, move):
        if(self.type == move.type):
            return 1.5
        else:
            return 1.0
    
    def load_json(self,path):
        with open(path, "r") as f:
            return json.load(f)
    
    def get_type_effectiveness(self, move, opponent):
        type_matrix = [
                #NOR, GRASS, WATER, FIRE, ELECTRIC, STEEL
                [1,    1,     1,     1,   1,        0.5],  # NORMAL
                [1,    0.5,   0.5,   2,   1,        0.5],  # GRASS
                [1,    2,     0.5,   0.5, 1,        1],    # WATER
                [1,    0.5,   2,     0.5, 1,        2],    # FIRE
                [1,    0.5,   1,     1,   0.5,      1],    # ELECTRIC
                [1,    1,     1,     0.5, 1,        0.5]   # STEEL
            ]
        return type_matrix[opponent.type.value][move.type.value]

    def use_move(self, index, opponent):
        move = self.moveset[index]
        print(f"{self.name} used {self.moveset[index].name}!")
        # Base Damage = (((2L)/5)+2)*(P*A)/(50*D)) + 2 
        damage = self.get_damage(move, opponent) 
        opponent.stats[Stats.Health.value] -= damage
        print(f"It dealt {damage} damage to {opponent.name}!")
        print(f"{opponent.name} has {opponent.stats[Stats.Health.value]} HP left!")

    def __str__(self) -> str:
        return "Your Pokemon is: " + self.name + " and it is a " + self.type.name +" type!" 
    
    




 