from classes import Stats

def pokemon_battle(pokemon1, pokemon2):
    # who go first
    while(pokemon1.doa_status and pokemon2.doa_status):
        if pokemon1.stats[Stats.Speed.value] > pokemon2.stats[Stats.Speed.value]:
            pokemon1.fight(pokemon2)
            check_status(pokemon2)
            if not pokemon2.doa_status:
                break
            pokemon2.fight(pokemon1) 
            check_status(pokemon1)
            if not pokemon1.doa_status:
                break
        else:
            pokemon2.fight(pokemon1)
            check_status(pokemon1)
            if not pokemon1.doa_status:
                break
            pokemon1.fight(pokemon2)   
            check_status(pokemon2)
            if not pokemon2.doa_status:
                break
        print("\nThe battle rages on.....\n")
    

def compute_damage(offensive, target):
    # Base Damage = (((2L)/5)+2)*(P*A)/(50*D)) + 2 
    base_damage = (((2*offensive.level)/5)+2)*((100*offensive.stats[0])/(50*target.stats[1])) + 2
    print(base_damage)

def check_status(pokemon):
    '''
    This function checks the pokemons health
    if the pokemon's health reaches 0 then change the status of the pokemon to Fainted
    '''
    if pokemon.stats[Stats.Health.value] <= 0:
        pokemon.doa_status = False
        print(f"{pokemon.name} has FAINTED!")

def declare_winner(pokemon1,pokemon2):
    return 0


