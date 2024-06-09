# Copyright (c) AWildDevAppears

from offspringengine.models.character import Character
from enum import Enum


class RoomType(Enum):
    UNASSIGNED = 0
    BOSS = 1
    COMBAT = 2
    LOOT  = 3


class Room():
    def __init__(self) -> None:
        self.type = RoomType.UNASSIGNED
        self.enemies: list[Character] = []
        self.boss: Character | None = None

