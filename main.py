from classes import Pokemon, Type
import battles


charmander = Pokemon("Charmander", Type.FIRE, [10,10,30,40], ["Scratch", "Growl", "Ember", "Metal Claw"])
bulbasaur = Pokemon("Bulbasaur", Type.GRASS, [8,15,25,50], ["Tackle", "Leer", "Razor Leaf", "Absorb"])

battles.pokemon_battle(charmander,bulbasaur)


