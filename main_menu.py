from classes import Pokemon, Type
import random

def main_menu():
    start_pokemon_dict = {1: "Charmander", 2: "Squirtle", 3: "Bulbasaur", 4: "Pikachu"}
    list_of_starter_pokemon = [key for key in start_pokemon_dict.keys()]
    print("\n========================================\n")
    print(" \n WELCOME TO THE TEXT BASED POKEMON GAME BATTLE SIMULATOR \n")
    print(" Choose Your Starter Pokemon !")
    print(" \n 1. Charmander  2. Squirtle \n")
    print(" \n 3. Bulbasaur 4. Pikachu \n")
    user_input = int(input())
    list_of_starter_pokemon.remove(user_input)
    opponent = random.choice(list_of_starter_pokemon)
    user_pokemon_1 = initialise_starter(user_input)
    opponent_pokemon_1 = initialise_starter(opponent)
    show_selections(user_pokemon_1, opponent_pokemon_1)
    print("\n========================================\n")

def show_selections(user_pokemon, opp_pokemon):
    print(f"You have chosen {user_pokemon.name}!")
    print(f"Your Opponent is {opp_pokemon.name}!")

def initialise_starter(my_var):
    match my_var:
        case 1:
            return charmander_init()
        case 2:
            return squirtle_init()
        case 3:
            return bulbasaur_init()
        case 4:
            return pikachu_init()

def charmander_init():
    return Pokemon("Charmander", Type.FIRE, [10,10,30,40], ["Scratch", "Growl", "Ember", "Metal Claw"])

def bulbasaur_init():
    return Pokemon("Bulbasaur", Type.GRASS, [8,15,25,50], ["Tackle", "Leer", "Razor Leaf", "Absorb"])

def squirtle_init():
    return Pokemon("Squirtle", Type.WATER, [12,20,20,30], ["Pound", "Tail Whip", "Water Gun", "Bubble"])

def pikachu_init():
    return Pokemon("Pikachu", Type.ELECTRIC, [15,8,50,60], ["Scratch", "Tail Whip", "Thunderbolt", "Iron Tail"])