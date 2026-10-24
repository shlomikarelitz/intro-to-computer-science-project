from Pikachu import Pikachu
from Charmander import Charmander
from Charizard import Charizard
from Wartortle import Wartortle
from Trainer import Trainer
from Battle import Battle
charzy = Charizard("charzy", 45, "fire", 37, 93, 93, 82)
pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)
ash = Trainer("ash", 18, 6.0, [charzy, pika])
print(ash)
# The Trainer ash is 18 years old and has the following pokemons (2 in
# total):
#  The Charizard charzy of level 37 with 93 HP
#  The Pikachu pika of level 32 with 35 HP
warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)
misty = Trainer("misty", 18, 5.5, [warty, charmy])
print(misty)
# The Trainer misty is 18 years old and has the following pokemons (2 in total):
# The Wartortle warty of level 30 with 78 HP
#  The Charmander charmy of level 15 with 57 HP
battle = Battle(ash, misty)
battle.total_battle()
# The battle ended with a draw
print(misty)
# The Trainer misty is 18 years old and has the following pokemons (2 in
# total):
#  The Wartortle warty of level 30 with 0 HP
#  The Charmander charmy of level 15 with -6 HP
print(ash)
# The Trainer ash is 18 years old and has the following pokemons (2 in
# total):
#  The Charizard charzy of level 37 with -12 HP
#  The Pikachu pika of level 32 with 2 HP
