from classes import Stats, Type

def pokemon_battle(pokemon1, pokemon2):
    # who go first
    display_fight_start(pokemon1, pokemon2)
    while(pokemon1.doa_status and pokemon2.doa_status):
        display_battle_state(pokemon1, pokemon2)
        if pokemon1.stats[Stats.Speed.value] > pokemon2.stats[Stats.Speed.value]:
            pokemon1.fight(pokemon2)
            check_status(pokemon2,pokemon1)
            if not pokemon2.doa_status:
                break
            pokemon2.fight(pokemon1) 
            check_status(pokemon1,pokemon2)
            if not pokemon1.doa_status:
                break
        else:
            pokemon2.fight(pokemon1)
            check_status(pokemon1,pokemon2)
            if not pokemon1.doa_status:
                break
            pokemon1.fight(pokemon2)   
            check_status(pokemon2,pokemon1)
            if not pokemon2.doa_status:
                break
        print("\nThe battle rages on.....\n")
    

def compute_damage(offensive, target):
    # Base Damage = (((2L)/5)+2)*(P*A)/(50*D)) + 2 
    base_damage = (((2*offensive.level)/5)+2)*((100*offensive.stats[0])/(50*target.stats[1])) + 2
    print(base_damage)

def check_status(pokemon, opponent):
    '''
    This function checks the pokemons health
    if the pokemon's health reaches 0 then change the status of the pokemon to Fainted
    '''
    if pokemon.stats[Stats.Health.value] <= 0:
        pokemon.doa_status = False
        print(f"{pokemon.name} has FAINTED!")
        print(f"{opponent.name} is the winner !!!")

def declare_winner(pokemon1,pokemon2):
    return 0

def display_battle_state(pokemon1, pokemon2):
    print("\n========================================\n")
    print(f"{pokemon1.name} has {pokemon1.stats[Stats.Health.value]} left!\n")
    print(f"{pokemon2.name} has {pokemon2.stats[Stats.Health.value]} left!\n")
    print("\n========================================\n")

def display_fight_start(pokemon1, pokemon2):
    print("\n========================================\n")
    print(f"{pokemon2.name} has challenged you to a battle!")
    print(f"Type: {pokemon2.type.name}")
    print(f"Health: {pokemon2.stats[Stats.Health.value]}")
    print(f"Atack: {pokemon2.stats[Stats.Attack.value]}")
    print(f"Defence: {pokemon2.stats[Stats.Defence.value]}")
    print(f"Speed: {pokemon2.stats[Stats.Speed.value]}")
    print("\n")
    print("VS\n")
    print("\n")
    print(f"{pokemon1.name} will fight for you!")
    print(f"Type: {pokemon1.type.name}")
    print(f"Health: {pokemon1.stats[Stats.Health.value]}")
    print(f"Atack: {pokemon1.stats[Stats.Attack.value]}")
    print(f"Defence: {pokemon1.stats[Stats.Defence.value]}")
    print(f"Speed: {pokemon1.stats[Stats.Speed.value]}")   

