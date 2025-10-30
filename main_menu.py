from classes import Pokemon, Type
import random

def main_menu():
    list_of_starter_pokemon = [1,2,3,4]
    print("\n========================================\n")
    print(" \n WELCOME TO THE TEXT BASED POKEMON GAME BATTLE SIMULATOR \n")
    print(" Choose Your Starter Pokemon !")
    print(" \n 1. Charmander  2. Squirtle \n")
    print(" \n 3. Bulbasaur 4. Pikachu \n")
    user_input = int(input())
    list_of_starter_pokemon.remove(user_input)
    opponent = random.choice(list_of_starter_pokemon)
    match user_input:
        case 1:
            user_pokemon_1 = Pokemon("Charmander", Type.FIRE, [10,10,30,40], ["Scratch", "Growl", "Ember", "Metal Claw"])
            opponent_pokemon_1 = Pokemon("Bulbasaur", Type.GRASS, [8,15,25,50], ["Tackle", "Leer", "Razor Leaf", "Absorb"])
            show_selections(user_pokemon_1, opponent_pokemon_1)
        case 2:
            user_pokemon_1 = Pokemon("Charmander", Type.FIRE, [10,10,30,40], ["Scratch", "Growl", "Ember", "Metal Claw"])
            opponent_pokemon_1 = Pokemon("Bulbasaur", Type.GRASS, [8,15,25,50], ["Tackle", "Leer", "Razor Leaf", "Absorb"])
            show_selections(user_pokemon_1, opponent_pokemon_1)

    print("\n========================================\n")

def show_selections(user_pokemon, opp_pokemon):
    print(f"You have chosen {user_pokemon.name}!")
    print(f"Your Opponent is {opp_pokemon.name}!")