from offspringengine.models.equipment import Equipment
from tinydb import TinyDB
from tinydb.queries import Query
from tinydb.table import Document

db = TinyDB("./database.json")
items_table = db.table("ITEMS", cache_size=30)
maps_table = db.table("MAPS", cache_size=30)


def get_item_by_id(id: str) -> Equipment:
    item: Equipment = Query()
    return items_table.search(item.id == id)[0]

def get_all_items() -> list[Equipment]:
    return items_table.all()
