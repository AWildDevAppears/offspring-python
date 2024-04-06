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


class Item(persistent.Persistent):
    def __init__(self, name: str, description: str) -> None:
        super().__init__()
        self.name: str = name
        self.description = description


class Equipment(Item):
    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.slot = EquipSlot.NONE
        self.rarity = EquipLevels.COMMON
        self.mods: list[EquipModifier] = []

    def full_name(self):
        match self.rarity:
            case EquipLevels.DAMAGED:
                return f"damaged {self.name}"
            case EquipLevels.UNCOMMON:
                return f"uncommon {self.name}"
            case EquipLevels.RARE:
                return f"rare {self.name}"
            case EquipLevels.LEGENDARY:
                return f"legendary {self.name}"
            case EquipLevels.UNIQUE:
                return f"unique {self.name}"
            case _:
                return self.name


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


class ArmorChest(Armor):
    def __init__(self, name: str, description: str, defence: int) -> None:
        super().__init__(name, description, defence)
        self.slot = EquipSlot.CHEST


class ArmorHelmet(Armor):
    def __init__(self, name: str, description: str, defence: int) -> None:
        super().__init__(name, description, defence)
        self.slot = EquipSlot.HEAD


class ArmorLegs(Armor):
    def __init__(self, name: str, description: str, defence: int) -> None:
        super().__init__(name, description, defence)
        self.slot = EquipSlot.LEGS


class ArmorFeet(Armor):
    def __init__(self, name: str, description: str, defence: int) -> None:
        super().__init__(name, description, defence)
        self.slot = EquipSlot.FEET


class ArmorGloves(Armor):
    def __init__(self, name: str, description: str, defence: int) -> None:
        super().__init__(name, description, defence)
        self.slot = EquipSlot.GLOVES


class EquipTrinket(Equipment):
    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.slot = EquipSlot.TRINKET


type ArmorType = ArmorHelmet | ArmorLegs | ArmorGloves | ArmorFeet | ArmorChest
type EquipmentType = ArmorType | Weapon | EquipTrinket


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
