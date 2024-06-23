from offspringengine.models.character import Character
from offspringengine.models.offspring_error import OffspringErrorCodes, OffspringResponse


class HubState(object):
    gold: int = 0
    equipment: list[str] = []
    equipment_max_size: int = 128

    all_cards: list[str] = []
    current_deck: list[str] = []
    current_deck_max_size: int = 24

    character: Character | None = None


hub_state = HubState()


def assign_character(char: Character | None) -> OffspringResponse:
    if char is not None and hub_state.character is not None:
        return OffspringResponse(True, message="Character already set")

    hub_state.character = char
    return OffspringResponse(False)


def hub_get_state() -> OffspringResponse:
    return OffspringResponse(False, data=hub_state)


def inventory_add_item(item: str) -> OffspringResponse:
    if len(hub_state.equipment) >= hub_state.equipment_max_size:
        return OffspringResponse(True, message="Inventory full", error_ref=OffspringErrorCodes.HUB_INVENTORY_FULL)

    hub_state.equipment.append(item)
    return OffspringResponse(False)


# TODO: Equip items
def inventory_equip_item(item: str):
    pass
