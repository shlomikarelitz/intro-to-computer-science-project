from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name, catch_rate):
        if isinstance(name, str):
            self.__name=name
        else:
            raise TypeError
        if not isinstance(catch_rate, int):
            raise TypeError
        elif (catch_rate>45 or catch_rate<40):
            raise ValueError
        else:
            self.__catch_rate=catch_rate
    def get_name(self):
        return self.__name

    def get_catch_rate(self):
        return self.__catch_rate

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
    def get_effective_against_me(self):
        pass
    @abstractmethod
    def get_effective_against_others(self):
        pass
    @abstractmethod
    def get_hit_points(self):
        pass
    @abstractmethod
    def get_pokemon_type(self):
        pass
    @abstractmethod
    def level_up(self):
        pass
