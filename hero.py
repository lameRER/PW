import random


class Hero:

    @property
    def hp(self):
        return self._hp

    def __init__(self, hero):
        self._player_name = hero._player_name
        self._lvl = hero._lvl
        self._max_dp = 100
        self._max_hp = hero._max_hp
        self._max_mana = hero._max_mana
        self._dp = 0
        self._hp = hero._hp
        self._mana = hero._mana
        self._attack = hero._attack


    def set_dp(self):
        dp = int((self._max_dp >> 1) * 0.1)
        if self._dp + dp >= self._max_dp:
            self._dp += dp
            self._dp = self._dp - self._max_dp
            self.__lvl_up()
        else:
            self._dp += dp

    def __lvl_up(self):
        self._lvl += 1
        self._max_hp = self._max_hp + 2 * self._lvl
        self._max_mana = self._max_mana + 2 * self._lvl
        self._max_dp = (self._max_dp >> 1) * 3
        self._hp = self._max_hp
        self._mana = self._max_mana
        self._attack = self._attack + 1 * self._lvl

    def attack(self, hero):
        if self._hp > 0 and hero._hp > 0:
            damage = random.randint(1, self._attack)
            hero._hp = hero.__get_damage(damage)
            if hero._hp <= 0:
                self.set_dp()

    def __get_damage(self, damage):
        return self._hp - damage

    def __str__(self):
        return f"""
{self._player_name}
DP: {self._dp}/{self._max_dp}
lvl: {self._lvl}
HP: {self._hp}
mana: {self._mana}
attack: {self._attack}
"""
