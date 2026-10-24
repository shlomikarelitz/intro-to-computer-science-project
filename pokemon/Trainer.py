import copy
from Charmander import Charmander
from Charmeleon import Charmeleon
from Charizard import Charizard
from Pikachu import Pikachu
from Squirtle import Squirtle
from Wartortle import Wartortle
from Blastoise import Blastoise

class Trainer():
    def __init__(self, name, age, exp_modifier, pokemons_lst=None):
        if isinstance(name, str) and name!="":
            self.__name = name
        elif not isinstance(name,str):
            raise TypeError
        else:
            raise ValueError

        if isinstance(age, int) and age>15 and age <=120:
            self.__age = age
        elif not isinstance(age,int):
            raise TypeError
        else:
            raise ValueError

        if (isinstance(exp_modifier, float) or isinstance(exp_modifier,int)) and exp_modifier >=1.5 and exp_modifier <= 12.5:
            self.__exp_modifier = exp_modifier
        elif not isinstance(exp_modifier, float):
            raise TypeError
        else:
            raise ValueError
        if pokemons_lst is None:
            self.__pokemons_lst=[]
        else:
            self.__pokemons_lst=pokemons_lst

    def __len__(self):
        return len(self.__pokemons_lst)

    def __repr__(self):
        ls_of_trainer= f"The Trainer {self.__name} is {self.__age} years old and has the following pokemons ({self.__len__()} in total):"
        for pokemon in self.get_pokemon_lst():
            ls_of_trainer+= "\n    " + pokemon.__repr__()

        return ls_of_trainer

    def get_name(self):
        return copy.deepcopy(self.__name)

    def get_age(self):
        return copy.deepcopy(self.__age)

    def get_exp_modifier(self):
        return copy.deepcopy(self.__exp_modifier)

    def get_pokemon_lst(self):
        return copy.deepcopy(self.__pokemons_lst)

    def change_pokemon_lst(self, pokemon, pokemon_id):
        self.__pokemons_lst[pokemon_id] = pokemon

    def catch_pokemon(self, pokemon):
        capture_chances = pokemon.get_catch_rate()*self.get_exp_modifier()*(100-pokemon.get_hit_points())/100
        if capture_chances >50:
            print(self.get_name() + " caught " + pokemon.get_name())
            self.__pokemons_lst.append(pokemon)
        else:
            print(self.get_name()+ " couldn't catch " + str(pokemon.get_name()))

    def sum_of_lives(self):
        sum_lives=0
        for pokemon in Trainer.get_pokemon_lst(self):
            sum_lives+=pokemon.get_hit_points()
        return sum_lives

    def __eq__(self, other):
        return Trainer.sum_of_lives(self)==Trainer.sum_of_lives(other)

    def __ne__(self, other):
        return Trainer.sum_of_lives(self)!=Trainer.sum_of_lives(other)

    def __gt__(self, other):
        return Trainer.sum_of_lives(self)>Trainer.sum_of_lives(other)

    def __lt__(self, other):
        return Trainer.sum_of_lives(self)<Trainer.sum_of_lives(other)

    def __ge__(self, other):
        return Trainer.sum_of_lives(self)>=Trainer.sum_of_lives(other)

    def __le__(self, other):
        return Trainer.sum_of_lives(self) <= Trainer.sum_of_lives(other)

    def __add__(self, other):
        if Trainer.__gt__(self, other):
            new_name = str(Trainer.get_name(self)) + "-" + str(Trainer.get_name(other))
        else:
            new_name = str(Trainer.get_name(other)) + "-" + str(Trainer.get_name(self))
        new_age=int((Trainer.get_age(self)+Trainer.get_age(other))/2)
        new_exp_modifier=float((Trainer.get_exp_modifier(self)+Trainer.get_exp_modifier(other))/2)
        if Trainer.__gt__(self, other):
            new_list_of_pokemons= Trainer.get_pokemon_lst(self)+Trainer.get_pokemon_lst(other)
        else:
            new_list_of_pokemons= Trainer.get_pokemon_lst(other)+Trainer.get_pokemon_lst(self)
        return Trainer(new_name,new_age,new_exp_modifier,new_list_of_pokemons)
