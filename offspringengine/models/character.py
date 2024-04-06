import persistent
from .equipment import (
    ArmorChest,
    ArmorFeet,
    ArmorGloves,
    ArmorHelmet,
    ArmorLegs,
    EquipTrinket,
)


class Character(persistent.Persistent):
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.attack = 0
        self.base_defence = 0
        self.health = 0
        self.base_healthMax = 0

        self.head_armor: ArmorHelmet | None = None
        self.body_armor: ArmorChest | None = None
        self.leg_armor: ArmorLegs | None = None
        self.feet_armor: ArmorFeet | None = None
        self.hand_armor: ArmorGloves | None = None
        self.trinket: EquipTrinket | None = None

    def get_is_dead(self):
        return self.health == 0

    def get_defence(self):
        defence = self.base_defence

        if self.head_armor is not None:
            defence += self.head_armor.defence

        if self.body_armor is not None:
            defence += self.body_armor.defence

        if self.leg_armor is not None:
            defence += self.leg_armor.defence

        if self.feet_armor is not None:
            defence += self.feet_armor.defence

        if self.hand_armor is not None:
            defence += self.hand_armor.defence

        return defence
