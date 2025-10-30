import random 

def display_moveset(pokemon):
        print("\n========================================\n")
        print(f"1. {pokemon.moveset[0]}    2. {pokemon.moveset[1]}\n")
        print(f"3. {pokemon.moveset[2]}    4. {pokemon.moveset[3]}\n")
        print("\n========================================\n")

def display_move_used(pokemon,user_input):
    print("\n========================================\n")
    match user_input:
        case 1:
            print(f"{pokemon.name} used {pokemon.moveset[0]}!")
        case 2:
            print(f"{pokemon.name} used {pokemon.moveset[1]}!")
        case 3:
            print(f"{pokemon.name} used {pokemon.moveset[2]}!")
        case 4:
            print(f"{pokemon.name} used {pokemon.moveset[3]}!")
    print("\n========================================\n")

