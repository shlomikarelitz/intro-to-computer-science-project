from Pikachu import Pikachu
from Charmander import Charmander
from Charmeleon import Charmeleon
from Charizard import Charizard
from Squirtle import Squirtle
from Wartortle import Wartortle
from Blastoise import Blastoise
from Trainer import Trainer
from Battle import Battle
charmilious = Charmeleon("charmilious", 42, "fire", 19, 60, 71, 68)
warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)
charzy = Charizard("charzy", 45, "fire", 35, 95, 94, 83)
ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
charizardious = Charizard("charizardious", 45, "fire", 37, 93, 93,
82)
squirtly = Squirtle("squirtly", 41, "water", 9, 55, 49, 72)
blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)
misty = Trainer("misty", 18, 5.5, [charizardious, squirtly,
blasty, charmy])
battle = Battle(misty, ash)
battle.total_battle()
# Trainer misty won the battle in 15 rounds
print(misty)
# # The Trainer misty is 18 years old and has the following pokemons (4 in
# # total):
# #  The Charizard charizardious of level 37 with -12 HP
# #  The Squirtle squirtly of level 9 with 3 HP
# #  The Blastoise blasty of level 37 with 4 HP
# #  The Charmander charmy of level 15 with 38 HP
# ash
# # The Trainer ash is 18 years old and has the following pokemons (4 in
# # total):
# #  The Charmeleon charmilious of level 19 with 6 HP
# #  The Wartortle warty of level 30 with 2 HP
# #  The Pikachu pika of level 32 with -2 HP
# #  The Charizard charzy of level 35 with 1 HP
# ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
# misty = Trainer("misty", 18, 5.5, [charizardious, squirtly,
# blasty, charmy])
# battle = Battle(ash, misty)
# battle.total_battle()
# # Trainer ash won the battle in 15 rounds
# misty
# # The Trainer misty is 18 years old and has the following pokemons (4 in
# # total):
# #  The Charizard charizardious of level 37 with 5 HP
# #  The Squirtle squirtly of level 9 with 5 HP
# #  The Blastoise blasty of level 37 with 4 HP
# #  The Charmander charmy of level 15 with 3 HP
# ash
# # The Trainer ash is 18 years old and has the following pokemons (4 in
# # total):
# #  The Charmeleon charmilious of level 19 with 5 HP
# #  The Wartortle warty of level 30 with 30 HP
# #  The Pikachu pika of level 32 with -5 HP
# #  The Charizard charzy of level 35 with -2 HP
