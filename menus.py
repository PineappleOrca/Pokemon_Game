def display_moveset(pokemon):
        print("\n========================================\n")
        print(f"1. {pokemon.moveset[0].name}    2. {pokemon.moveset[1].name}\n")
        print(f"3. {pokemon.moveset[2].name}    4. {pokemon.moveset[3].name}\n")
        print("\n========================================\n")

def display_move_used(pokemon,user_input):
    print("\n========================================\n")
    match user_input:
        case 1:
            print(f"{pokemon.name} used {pokemon.moveset[0].name}!")
        case 2:
            print(f"{pokemon.name} used {pokemon.moveset[1].name}!")
        case 3:
            print(f"{pokemon.name} used {pokemon.moveset[2].name}!")
        case 4:
            print(f"{pokemon.name} used {pokemon.moveset[3].name}!")
    print("\n========================================\n")

