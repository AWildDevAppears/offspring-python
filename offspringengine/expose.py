from webview import Window

from offspringengine.state.dungeon_state import dungeon_get_deck, dungeon_next_location, dungeon_next_round, dungeon_state_init


def expose_to(window: Window):
    # Quest view
    window.expose(dungeon_state_init, dungeon_next_round, dungeon_next_location, dungeon_get_deck)
