import ZODB, ZODB.FileStorage
from ZODB.DB import Connection


class DB:

    def __init__(self):
        storage = ZODB.FileStorage.FileStorage("ofsspring.db")
        db = ZODB.DB(storage)
        self.connection: Connection = db.open()


current = DB()
