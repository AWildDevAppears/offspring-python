from tinydb import TinyDB
from tinydb.queries import Query
from tinydb.table import Document

db = TinyDB("./database.json")
items_table = db.table("ITEMS", cache_size=30)
maps_table = db.table("MAPS", cache_size=30)


def get_item_by_id(id: str) -> list[Document]:
    item = Query()
    return items_table.search(item.id == id)[0]
