from typing import cast
import persistent
from .equipment import (
    Armor,
    EquipSlot,
    EquipTrinket,
    Equipment,
    Weapon,
)

class CharacterModifier:
    def __init__(self) -> None:
        self.name = ""


class Pawn(persistent.Persistent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.attack = 0
        self.base_defence = 0
        self.health = 0
        self.base_health_max = 0

        self.modifiers: list[CharacterModifier] = []

    def get_is_dead(self):
        return self.health <= 0


class Character(Pawn):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.head_armor: Armor | None = None
        self.body_armor: Armor | None = None
        self.leg_armor: Armor | None = None
        self.feet_armor: Armor | None = None
        self.hand_armor: Armor | None = None
        self.trinket: EquipTrinket | None = None
        self.weapon_slot: Weapon | None = None

    def equip(self, equip: Equipment):
        match(equip.slot):
            case EquipSlot.WEAPON:
                self.weapon_slot = cast(Weapon, equip)
                return
            case EquipSlot.CHEST:
                self.body_armor = cast(Armor, equip)
                return
            case EquipSlot.HEAD:
                self.head_armor = cast(Armor, equip)
                return
            case EquipSlot.LEGS:
                self.leg_armor = cast(Armor, equip)
                return
            case EquipSlot.FEET:
                self.feet_armor = cast(Armor, equip)
                return
            case EquipSlot.GLOVES:
                self.hand_armor = cast(Armor, equip)
                return
            case EquipSlot.TRINKET:
                self.trinket = cast(EquipTrinket, equip)
                return
            case _:
                pass

    def unequip(self, slot: EquipSlot):
        match(slot):
            case EquipSlot.WEAPON:
                item = self.weapon_slot
                self.weapon_slot = None
                return item
            case EquipSlot.CHEST:
                item = self.body_armor
                self.body_armor = None
                return item
            case EquipSlot.HEAD:
                item = self.head_armor
                self.head_armor = None
                return item
            case EquipSlot.LEGS:
                item = self.leg_armor
                self.leg_armor = None
                return item
            case EquipSlot.FEET:
                item = self.feet_armor
                self.feet_armor = None
                return item
            case EquipSlot.GLOVES:
                item = self.hand_armor
                self.hand_armor = None
                return item
            case EquipSlot.TRINKET:
                item = self.trinket
                self.trinket = None
                return item
            case _:
                pass

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

class Enemy(Pawn):
    def __init__(self, name: str) -> None:
        super().__init__(name)

