import random

from offspringengine.models.card import Card, CardTarget
from offspringengine.models.character import Character, Pawn
from offspringengine.models.dungeon import Dungeon
from offspringengine.models.offspring_response import OffspringResponse
from offspringengine.models.room import Room, RoomType
from offspringengine.services.cards import create_deck_for


###
# - Init -
# Takes [player, enemy_pool, deck]
# - Generate loot pool -
# - Generate map -
# * Work out how many locations are in this dungeon
# * Decide how many loot rooms there will be
# * Add boss fight to end
# * Set room 1 as combat room
# * randomly inject loot rooms
# * mark all other rooms as combat rooms
# * add monsters to all combat rooms
# * set player location as room 1.
# - Combat -
# * - Player phase -
# * set player stamina (GROUP 1)
# * Deal player 7 cards
# * Player picks card (GROUP 2)
# * If target is enemy, player picks enemy
# * Card is played
# * reduce player stamina
# * Cards the player does not have enough stamina to play get disabled
# * If there are no more enemies jump to (GROUP 4)
# * At any point the player can "end turn", when pressed go to (GROUP 3)
# * Return to (GROUP 2)
# * - Enemy phase -
# * For each enemy: (GROUP 3)
# * Enemy picks and plays card
# * When no more enemies go to (GROUP 1)
# * If player dead go to (GROUP 5)
# * - Win - (GROUP 4)
# * Set player location as next room
# * If combat room go to (GROUP 1)
# * If loot room go to (GROUP 6)
# * If last room go to (GROUP 7)
# * - Lose - (GROUP 5)
# * Purge dungeon
# * Send player to character select
# * - Loot room - (GROUP 6)
# * Generate loot for room
# * Show loot to player
# * Add loot to player inventory
# * Go to (GROUP 4)
# - Boss fight - (GROUP 7)
# * Load boss combat scenario
# * If lose fight go to (GROUP 5)
# * If win fight:
# * Add equipment to hub inventory
# * Add gold to hub gold
# * ...
# * Show win screen
# * When player presses continue button return to lobby
###
class DungeonState(object):
    gold: int = 0
    inventory: list[str] = []
    player_party: list[Character] = []
    enemy_party: list[Pawn] = []
    deck: list[Card] = []
    current_hand: list[Card] = []

    round: int = 0

    ## Dungeon
    enemy_pool: list[str] = []
    dungeon: list[Room] = []
    location_idx: int = 0

class DungeonRes:
    def __init__(self, cont: bool) -> None:
        self.cont = cont


dungeon_state = DungeonState()


# Takes [player, enemy_pool, deck]
# - Generate loot pool -
# - Generate map -
# * Work out how many locations are in this dungeon
# * Decide how many loot rooms there will be
# * Add boss fight to end
# * Set room 1 as combat room
# * randomly inject loot rooms
# * mark all other rooms as combat rooms
# * add monsters to all combat rooms
# * set player location as room 1.

## @Public
def dungeon_state_init():
    dungeon_state.player_party = []
    dungeon_state.deck = create_deck_for(["C:001", "C:001", "C:001", "C:001", "C:001", "C:002", "C:002", "C:002", "C:003", "C:003"])
    dungeon_state.enemy_pool = create_enemy_list_for(["E:001"])
    #TODO: loot_pool

    map_size = random.randint(6, 12)
    loot_room_count = random.randint(0, 2)

    dungeon_state.dungeon = []

    for idx in range(map_size):
        dungeon_state.dungeon.append(Room())

    dungeon_state.dungeon[0] = prepare_combat_room(dungeon_state.dungeon[0])
    dungeon_state.dungeon[len(dungeon_state.dungeon) - 1] = prepare_boss_room(dungeon_state.dungeon[len(dungeon_state.dungeon) - 1])

    # Add all of our loot rooms
    for idx in range(loot_room_count):
        added = False
        while not added:
            location = random.randint(1, map_size - 1)
            room = dungeon_state.dungeon[location]

            if room.type is RoomType.UNASSIGNED:
                room.type = RoomType.LOOT
                added = True

    # Fill out everything else with combat rooms
    for room in dungeon_state.dungeon:
        if room.type is RoomType.UNASSIGNED:
            room = prepare_combat_room(room)

    dungeon_state.location_idx = 0


def dungeon_next_round() -> DungeonRes:
    dungeon_state.round += 1

    # Trigger all modifiers to player

    # Trigger all modifiers to enemies

    # Trigger all modifiers to arena

    # Handle player combat

    # Handle enemy combat

    return on_finish_combat_round()


def dungeon_next_location():
    pass


def dungeon_get_deck():
    return OffspringResponse(False, data={
        "deck": dungeon_state.deck
    })

## Private
def prepare_combat_room(room: Room):
    room.type = RoomType.COMBAT
    # TODO: Add monsters to rooms
    return room


def prepare_boss_room(room: Room):
    room.type = RoomType.BOSS
    return room


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


def use_card(card: Card, caster: Character, target_label: CardTarget, target_list: list[Character] = []):
    match target_label:
        case CardTarget.SELF:
            caster.apply_card(card)
            return
        case CardTarget.ENEMY:
            for target in target_list:
                target.apply_card(card)

            return
        case CardTarget.ALL:
            caster.apply_card(card)

            for enemy in dungeon_state.enemy_party:
                enemy.apply_card(card)

            return
        case CardTarget.ENEMY_ALL:
            for enemy in dungeon_state.enemy_party:
                enemy.apply_card(card)

                return

        case CardTarget.ARENA:
            # Apply to dungeon
            return

        case CardTarget.SPELL:
            # Apply to next spell
            return



