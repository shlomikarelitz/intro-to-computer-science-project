from Pokemon import Pokemon
from abc import ABC, abstractmethod
import copy


class Fire(Pokemon, ABC):
    def __init__(self, name, catch_rate, pokemon_type):
        super().__init__(name, catch_rate)
        if isinstance(pokemon_type, str) and pokemon_type == "fire":
            self.__pokemon_type = pokemon_type
        else:
            raise ValueError

    def get_pokemon_type(self):
        return copy.copy(self.__pokemon_type)

    def get_effective_against_me(self):
        get_against_me = copy.copy(["water"])
        return get_against_me

    def get_effective_against_others(self):
        effective_against_others = copy.copy([])
        return effective_against_others

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def absorb(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def can_fight(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def get_defense_power(self):
        pass

    @abstractmethod
    def get_hit_points(self):
        pass

    @abstractmethod
    def level_up(self):
        pass
