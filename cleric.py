from elf import Elf


class Cleric(Elf):
    def __init__(self, player_name):
        self._player_name = player_name
        self._lvl = 1
        self._max_hp = 50
        self._max_mana = 70
        self._hp = self._max_hp
        self._mana = self._max_mana
        self._attack = 4
        super().__init__(self)
