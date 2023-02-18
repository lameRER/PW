from untamed import Untamed


class Barbarian(Untamed):
    def __init__(self, player_name):
        self._player_name = player_name
        self._lvl = 1
        self._max_hp = 85
        self._max_mana = 35
        self._hp = self._max_hp
        self._mana = self._max_mana
        self._attack = 9
        super().__init__(self)
