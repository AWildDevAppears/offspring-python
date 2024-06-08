
from offspringengine.models.card import Card
from offspringengine.models.character import Character


class DungeonState(object):
    gold: int = 0
    inventory: list[str] = []
    player_party: list[Character] = []
    enemy_party: list[Character] = []
    deck: list[Card] = []
    current_hand: list[Card] = []

    round: int = 0

    ## Dungeon
    enemy_pool: list[Character] = []

class DungeonRes:
    def __init__(self, cont: bool) -> None:
        self.cont = cont


dungeon_state = DungeonState()


# TODO: Build dungeon object
def dungeon_state_init(player_party: list[Character]):
    dungeon_state.player_party = player_party

def next_round() -> DungeonRes:
    dungeon_state.round += 1

    # Trigger all modifiers to player

    # Trigger all modifiers to enemies

    # Trigger all modifiers to arena

    # Handle player combat

    # Handle enemy combat

    return on_finish_combat_round()


def next_location():
    pass


def purge():
    dungeon_state.gold = 0
    dungeon_state.player_party = []
    dungeon_state.round = 0
    dungeon_state.inventory = []
    dungeon_state.enemy_party = []
    dungeon_state.enemy_pool = []
    dungeon_state.deck = []
    dungeon_state.current_hand = []


def on_finish_combat_round():
    player_party_is_alive = False

    for pawn in dungeon_state.player_party:
        if not pawn.get_is_dead():
            player_party_is_alive = True
            break

    if not player_party_is_alive:
        return DungeonRes(False)

    enemy_party_is_alive = False

    for pawn in dungeon_state.enemy_party:
        if not pawn.get_is_dead():
            enemy_party_is_alive = True
            break

    if not enemy_party_is_alive:
        return DungeonRes(False)

    return DungeonRes(True)

