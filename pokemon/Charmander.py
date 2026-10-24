from Fire import Fire
from abc import ABC, abstractmethod
import copy
from Charmeleon import Charmeleon

class Charmander(Fire, ABC):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):
        super().__init__(name, catch_rate, pokemon_type)
        if level > 15 or level<1:
            raise ValueError
        elif not isinstance(level, int):
            raise TypeError
        else:
            self.__level=level

        if hit_points>57 or hit_points<39:
            raise ValueError
        elif not isinstance(hit_points, int):
            raise TypeError
        else:
            self.__hit_points=hit_points
            self.HP=copy.deepcopy(self.__hit_points)

        if attack_power > 63 or attack_power < 52:
            raise ValueError
        elif not isinstance(attack_power, int):
            raise TypeError
        else:
            self.__attack_power=attack_power

        if defense_power > 57 or defense_power < 43:
            raise ValueError
        elif not isinstance(defense_power, int):
            raise TypeError
        else:
            self.__defense_power=defense_power

    def __repr__(self):
        return "The Charmander "+ self.get_name() + " of level "+ str(self.__level)+ " with "+ \
                str(self.__hit_points) + " HP"

    def get_hit_points(self):
        return copy.copy(self.__hit_points)

    def get_defense_power(self):
        return copy.deepcopy(self.__defense_power)

    def can_fight(self):
        if int(self.HP/10) >= self.__hit_points:            return False
        else:
            return True

    def get_damage(self, other):
        eff=0.5
        damage = int((((2/5)*self.__level)+2)*(self.__attack_power/other.get_defense_power())*eff)
        return damage

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points-=int(self.HP/10)
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        if level_gain<0:
            return
        elif level_gain<=16:
            self.__level+=level_gain
            if self.__level>15:
                return self.evolve()
            else:
                return None
        else:
            return None

    def evolve(self):
        check_level=self.__hit_points+19
        if not (check_level<77 or check_level<58):
            check_level=58

        chrmander_develop=Charmeleon(self.get_name(), self.get_catch_rate(),self.get_pokemon_type(),\
        self.__level,check_level, self.__attack_power+12, self.get_defense_power()+15)

        return chrmander_develop
