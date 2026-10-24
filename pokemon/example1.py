from Pikachu import Pikachu
from Blastoise import Blastoise
from Trainer import Trainer
from Battle import Battle
pika = Pikachu("pika", 40, "electric", 26, 90, 63, 85, 2)
blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
ash = Trainer("ash", 18, 6.0, [pika])
misty = Trainer("misty", 18, 5.5, [blasty])
battle = Battle(ash, misty)
battle_score = battle.dual_battle(0, 0)
print(battle_score)
# (4, 1)
print(ash)
# The Trainer ash is 18 years old and has the following pokemons (1 in
# total):
#  The Pikachu pika of level 26 with 33 HP
print(misty)
# The Trainer misty is 18 years old and has the following pokemons (1 in
# total):
#  The Blastoise blasty of level 37 with -2 HP
