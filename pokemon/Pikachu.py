from abc import ABC, abstractmethod
from Pokemon import Pokemon
from Electric import Electric
from Charmander import Charmander
from Charmeleon import Charmeleon
from Charizard import Charizard
from Squirtle import Squirtle
from Wartortle import Wartortle
from Blastoise import Blastoise
import copy

class Pikachu(Electric, ABC):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power, friendship):
        super().__init__(name, catch_rate, pokemon_type)
        if level > 32 or level<1:
            raise ValueError
        elif not isinstance(level, int):
            raise TypeError
        else:
            self.__level=level

        if hit_points>99 or hit_points<35:
            raise ValueError
        elif not isinstance(hit_points, int):
            raise TypeError
        else:
            self.__hit_points=hit_points
            self.HP=copy.deepcopy(self.__hit_points)

        if attack_power > 99 or attack_power < 55:
            raise ValueError
        elif not isinstance(attack_power, int):
            raise TypeError
        else:
            self.__attack_power=attack_power

        if defense_power > 99 or defense_power < 40:
            raise ValueError
        elif not isinstance(defense_power, int):
            raise TypeError
        else:
            self.__defense_power=defense_power

        if friendship > 5 or friendship < 1:
            raise ValueError
        elif not isinstance(friendship, int):
            raise TypeError
        else:
            self.__frienship=friendship

    def __repr__(self):
        return "The Pikachu "+ self.get_name() + " of level " + str(self.__level)+ " with "+ \
                str(self.__hit_points) + " HP"

    def get_hit_points(self):
        return copy.copy(self.__hit_points)

    def get_defense_power(self):
        return copy.copy(self.__defense_power)

    def can_fight(self):
        if int(self.HP/10) >= self.__hit_points:            return False
        else:
            return True

    def get_damage(self, other):
        if other.get_pokemon_type()== "water":
            eff=2
        else:
            eff=0.5
        damage=int((((2/5)*self.__level)+2)*(self.__attack_power/ other.get_defense_power())*eff)+ self.__frienship
        return damage

    def attack(self, other):
        if Pikachu.can_fight(self) and other.can_fight():
            self.__hit_points-=int(self.HP/10)
            other.absorb(self.get_damage(other))
    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        temp_level = self.level + level_gain
        if level_gain <= 0:
            return
        elif (temp_level) <= 50:
            self.level += level_gain
        else:
            self.level = 50
