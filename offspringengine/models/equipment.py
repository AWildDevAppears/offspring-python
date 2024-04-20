from enum import Enum
import persistent


class EquipSlot(Enum):
    NONE = "none"
    CHEST = "chest"
    HEAD = "head"
    LEGS = "legs"
    FEET = "feet"
    GLOVES = "gloves"
    TRINKET = "trinket"
    WEAPON = "weapon"


class EquipLevels(Enum):
    DAMAGED = "damaged"
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    LEGENDARY = "legendary"
    UNIQUE = "unique"


class Equipment(persistent.Persistent):
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description = description
        self.slot = EquipSlot.NONE
        self.rarity = EquipLevels.COMMON
        self.mods: list[EquipModifier] = []

    def full_name(self):
        return f"{self.rarity} {self.name}"


class Weapon(Equipment):
    def __init__(
        self, name: str, description: str, min_damage: int = 0, max_damage: int = 0
    ) -> None:
        super().__init__(name, description)
        self.slot = EquipSlot.WEAPON
        self.min_damage = min_damage
        self.max_damage = max_damage


class Armor(Equipment):
    def __init__(self, name: str, description: str, defence: int = 0) -> None:
        super().__init__(name, description)
        self.defence = defence


class EquipTrinket(Equipment):
    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.slot = EquipSlot.TRINKET


type EquipmentType = Armor | Weapon | EquipTrinket


class EquipStatMod:
    def __init__(self, rarity: EquipLevels, max: int, min: int, slots: int) -> None:
        super().__init__()
        self.rarity = rarity
        self.stats_max = max
        self.stats_min = min
        self.slots = slots


class EquipModifier:
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.description = ""
        self.rarity = None
        self.element = None
        self.trigger = None
