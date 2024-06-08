from offspringengine.models.character import Character

class HubState(object):
    gold: int = 0
    equipment: list[str] = []
    all_cards: list[str] = []
    current_deck: list[str] = []
    character: Character | None = None

hub_state = HubState()

def assign_character(char: Character):
    hub_state.character = char
