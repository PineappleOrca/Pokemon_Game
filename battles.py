from classes import Stats

def pokemon_battle(pokemon1, pokemon2):
    # who go first
    while(pokemon1.stats[3] > 0 and pokemon2.stats[3] > 0):
        if pokemon1.stats[2] > pokemon2.stats[2]:
            pokemon1.fight(pokemon2)
            check_status(pokemon2)
            pokemon2.fight(pokemon1) 
            check_status(pokemon1)
        else:
            pokemon2.fight(pokemon1)
            check_status(pokemon1)
            pokemon1.fight(pokemon2)   
            check_status(pokemon2)

        print(pokemon1.name + " has " + str(pokemon1.stats[Stats.Health.value]) + " hp left!")
        print(pokemon2.name + " has " + str(pokemon2.stats[Stats.Health.value]) + " hp left!")
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
    if pokemon.stats[3] <= 0:
        pokemon.status = 0
        print(f"{pokemon.name} has FAINTED!")


