from Trainer import Trainer
from Charmander import Charmander
from Charmeleon import Charmeleon
from Charizard import Charizard
from Pikachu import Pikachu
from Squirtle import Squirtle
from Wartortle import Wartortle
from Blastoise import Blastoise
from Pokemon import Pokemon
import copy

class Battle():
    def __init__(self, trainer1, trainer2):
        if isinstance(trainer1, Trainer) and isinstance(trainer2, Trainer):
            self.__trainer1=trainer1
            self.__trainer2=trainer2
        else:
            raise TypeError

    def dual_battle(self, trainer1_pokemon_id, trainer2_pokemon_id):
        number_of_rounds=0
        ls1=copy.deepcopy(self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id])
        ls2=copy.deepcopy(self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id])
        while ls1.can_fight() and ls2.can_fight():
            number_of_rounds += 1
            ls1.attack(ls2)
            if ls2.can_fight():
                ls2.attack(ls1)
            else:
                self.__trainer1.change_pokemon_lst(ls1, trainer1_pokemon_id)
                self.__trainer2.change_pokemon_lst(ls2, trainer2_pokemon_id)
                if ls1.can_fight():
                    return (number_of_rounds,1)
                else:
                    return (number_of_rounds,0)
        if ls1.can_fight():
            winner_is = 1
        elif ls2.can_fight():
            winner_is = 2
        else:
            winner_is = 0

        self.__trainer1.change_pokemon_lst(ls1,trainer1_pokemon_id)
        self.__trainer2.change_pokemon_lst(ls2,trainer2_pokemon_id)

        my_ls_tuple=[number_of_rounds,winner_is]
        print(my_ls_tuple)
        return tuple(my_ls_tuple)

    def there_is_pokemon_can_fight(self, trainer):
        for pokemon in trainer.get_pokemon_lst():
            if pokemon.can_fight():
                return True
        return False

    def return_pokemon_index(self, trainer):
        list_of_trainer=trainer.get_pokemon_lst()
        for pokemon in list_of_trainer:
            if pokemon.can_fight():
                index_of_pokemon=list_of_trainer.index(pokemon)
                return index_of_pokemon

    def the_best_pokemon_ind(self, pokemon1, trainer):
        pokemon_lst=trainer.get_pokemon_lst()
        corrent_one=0
        temp=0
        for pokemon in pokemon_lst:
            if pokemon.can_fight():
                corrent_one=pokemon_lst.index(pokemon)
                break
        for pokemon in pokemon_lst[corrent_one:]:
            if (pokemon.get_damage(pokemon1) >= temp) and pokemon.can_fight():
                corrent_one=pokemon_lst.index(pokemon)
                temp=pokemon.get_damage(pokemon1)
        return corrent_one


    def total_battle(self):
        total_rounds=0
        corrent_trainer=self.__trainer2
        pokemon_1=""
        pokemon_1_ind=0
        pokemon_2=""
        pokemon_2_ind=0
        is_one=False
        is_first=True
        middle_round=False
        while self.there_is_pokemon_can_fight(self.__trainer1) and self.there_is_pokemon_can_fight(self.__trainer2):
            if is_first:
                pokemon_1_ind=self.return_pokemon_index(self.__trainer1)
                pokemon_1=Trainer.get_pokemon_lst(self.__trainer1)[pokemon_1_ind]
                pokemon_2_ind =Battle.the_best_pokemon_ind(self, pokemon_1, corrent_trainer)
                pokemon_2=Trainer.get_pokemon_lst(self.__trainer2)[pokemon_2_ind]
            if middle_round and not is_one:
                pokemon_2_ind = Battle.the_best_pokemon_ind(self, pokemon_1, corrent_trainer)
                pokemon_2 = Trainer.get_pokemon_lst(self.__trainer2)[pokemon_2_ind]
            if is_one:
                corrent_trainer=self.__trainer1
                pokemon_1_ind=Battle.the_best_pokemon_ind(self, pokemon_2, corrent_trainer)
                pokemon_1=Trainer.get_pokemon_lst(self.__trainer1)[pokemon_1_ind]
                corrent_trainer=self.__trainer2
            battle_result = Battle.dual_battle(self, pokemon_1_ind, pokemon_2_ind)
            battle_result=list(battle_result)
            total_rounds+=battle_result[0]
            if battle_result[1]==0:
                is_first=True
                is_one=False
                middle_round=False
            if battle_result[1]==1:
                is_first = False
                is_one = False
                middle_round = True
            if battle_result[1]==2:
                is_first = False
                is_one = True
                middle_round = False
        if not Battle.there_is_pokemon_can_fight(self, self.__trainer1) and not Battle.there_is_pokemon_can_fight(self, self.__trainer2):
            print("The battle ended with a draw")
        elif Battle.there_is_pokemon_can_fight(self, self.__trainer1) and  not Battle.there_is_pokemon_can_fight(self, self.__trainer2):
            print(f"Trainer {self.__trainer1.get_name()} won the battle in {total_rounds} rounds")
        elif Battle.there_is_pokemon_can_fight(self, self.__trainer2) and not Battle.there_is_pokemon_can_fight(self, self.__trainer1):
            print(f"Trainer {self.__trainer2.get_name()} won the battle in {total_rounds} rounds")
