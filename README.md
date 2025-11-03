# Pokemon_Game
This is a project in Python to help me learn Object Oriented Programming and some Software Design. I will also try to write clean and efficient code. 

The aim of this initially is to set up a simple game of Pokemon where I can have features such as:
- Pick a starter Pokemon
- Pokemon exists within a database 
- Pokemon exist as objects and I can initialise them by looking up their names and relevant attributes
- The user or "trainer" can then use their pokemon to have a battle
- A Pokemon battle to feature similar setup to that of the main games
- The Pokemon will then gain experience points and level accordingly
- Levelling will have its appropriate effect on the pokemon's stats. 
- Create some AI trainers with sample pokemon and levels to have mock fights with

-> Current Status (WIP)
- Pokemon battles work as expected (minus correct damage calcs), moves and pokemon loaded from JSON files , opponent is assigned one random
pokemon after the user selects theirs from an initial set of 4

-> Things to add 
- Correct battle damage calcs (apply formula), type effectiveness etc, factor in accuracy
- pp tracking for moves
- improve display between turns to show pp and move types so the user can decide 
- add automated bot moves so it feels like the user is playing vs a bot 
- pokemon status moves + affect on stats
- maybe add support for player vs bot and player vs player, so player vs bot mode, the bot randomly picks a move, player vs player, two users subsequently use keystrokes for moves? 
- import pokeapi to populate database with moves and pokemon stats for improved accuracy, sqlite database for scalability
- 3v3 battle support, trainer class assemble teams and track