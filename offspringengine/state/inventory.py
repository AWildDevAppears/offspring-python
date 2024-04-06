import persistent
from connection import current


class InventoryDB(persistent.Persistent):

    def __init__(self) -> None:
        super().__init__()
        self.items = []
        self.gold = 0

    def commit(self):
        current.connection.commit(self)


current.connection.add(InventoryDB)
