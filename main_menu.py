from classes import Pokemon, Type, Moves
import battles
import random
import json

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
    print("\n========================================\n")
    print("============== FIGHT START ===============\n")
    battles.pokemon_battle(user_pokemon_1,opponent_pokemon_1)

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

def load_moves_from_json():
        path = "moves.json"
        with open(path, "r") as f:
            data = json.load(f)
        moves = {}
        for m in data:
            moves[m["name"]] = Moves(
                name=m["name"],
                power=m["power"],
                pp=m["pp"],
                type=Type[m["type"]],
                accuracy=m["accuracy"]
            )
        return moves

def charmander_init():
    move_db = load_moves_from_json()
    return Pokemon("Charmander", Type.FIRE, [10,10,30,40], [move_db["Scratch"], move_db["Growl"], move_db["Ember"], move_db["Metal Claw"]])

def bulbasaur_init():
    move_db = load_moves_from_json()
    return Pokemon("Bulbasaur", Type.GRASS, [8,15,25,50], [move_db["Tackle"], move_db["Leer"], move_db["Razor Leaf"], move_db["Absorb"]])

def squirtle_init():
    move_db = load_moves_from_json()
    return Pokemon("Squirtle", Type.WATER, [12,20,20,30], [move_db["Pound"], move_db["Tail Whip"], move_db["Water Gun"], move_db["Bubble"]])

def pikachu_init():
    move_db = load_moves_from_json()
    return Pokemon("Pikachu", Type.ELECTRIC, [15,8,50,60], [move_db["Scratch"], move_db["Tail Whip"], move_db["Thunderbolt"], move_db["Iron Tail"]])

# manually hardcoding the init of the moveset, eventually for scale and adding support for other pokemon have to make a database of some sort from an API

