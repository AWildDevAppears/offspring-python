import persistent
from BTrees._OOBTree import OOSet
from BTrees.Interfaces import ISet
from typing import List
from connection import current
from ..models.character import Character
from ..models.equipment import Item


class MainBase(persistent.Persistent):

    def __init__(self) -> None:
        pass


class EphemeralStore:

    def __init__(self) -> None:
        self.heldGold: int = 0
        self.held_items: List[Item] = []
        self.max_items = 15

    def clear(self):
        self.heldGold = 0
        self.helditems = []


class WorldDB(persistent.Persistent):

    def __init__(self) -> None:
        self.character: Character | None = None
        self.base: MainBase = MainBase()
        self.inventory: ISet = OOSet()
        self.gold: int = 0

    def commit(self):
        current.connection.commit(self)

    def consume(self, store: EphemeralStore):
        self.gold += store.heldGold

        for key in store.held_items:
            self.inventory.insert(key)


current.connection.root.world = WorldDB()
