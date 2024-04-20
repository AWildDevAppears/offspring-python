import random
from typing import cast

from offspringengine.services.database import get_item_by_id
from ..models.equipment import (
    Armor,
    EquipLevels,
    EquipSlot,
    EquipStatMod,
    EquipTrinket,
    Equipment,
    Weapon,
)

my_dummy_item = {
    "name": "my special helmet",
    "desc": "An item used for testing purposes",
    "slot": EquipSlot.HEAD,
    "defence": 10,
}


def get_equipable_level_effect():
    level = random.randint(0, 1000)

    if level <= 100:  # 100 - 10%
        return EquipStatMod(EquipLevels.DAMAGED, -5, -10, 0)
    if level <= 500:  # 400 - 40%
        return EquipStatMod(EquipLevels.COMMON, 5, 0, 0)
    if level <= 800:  # 300 - 30%
        return EquipStatMod(EquipLevels.UNCOMMON, 15, 10, 1)
    if level <= 900:  # 100 - 10%
        return EquipStatMod(EquipLevels.RARE, 20, 15, 2)
    if level <= 995:  # 95 - 9.5%
        return EquipStatMod(EquipLevels.LEGENDARY, 40, 15, 3)
    else:  # 5 - 0.5%
        return EquipStatMod(EquipLevels.UNIQUE, 60, 0, 4)


def get_equipable_for_slot(slot: EquipSlot, name: str, desc: str):
    match slot:
        case EquipSlot.TRINKET:
            return EquipTrinket(name, desc)
        case EquipSlot.WEAPON:
            return Weapon(name, desc, 0, 0)
        case _:
            armor = Armor(name, desc, 0)
            armor.slot = slot;
            return armor


def get_random_equippable():
    item: dict[str, str] = get_item_by_id("IT00000001")


    if item["type"] is EquipSlot.NONE:
        return None

    item_obj: Equipment = get_equipable_for_slot(
        item["type"], item["name"], item["description"]
    )
    item_level: EquipStatMod = get_equipable_level_effect()

    item_obj.rarity = item_level.rarity

    if item["type"] is EquipSlot.WEAPON:
        return cast(Weapon, item_obj)

    if item["type"] is EquipSlot.TRINKET:
        return cast(EquipTrinket, item_obj)

    # item["slot"] is an armor type:

    item_obj.defence = item["defence"] + random.randint(
        item_level.stats_min, item_level.stats_max
    )

    return cast(Armor, item_obj)
