from offspringengine.models.card import Card, CardModifierIndex
from offspringengine.models.equipment import Equipment
from tinydb import TinyDB
from tinydb.queries import Query
from tinydb.table import Document

db = TinyDB("./database.json")
items_table = db.table("ITEMS", cache_size=30)
item_mods_table = db.table("ITEM_MODIFIERS")
maps_table = db.table("MAPS", cache_size=30)
card_table = db.table("CARDS")

# - Items ------
def get_item_by_id(id: str) -> Equipment:
    item: Equipment = Query()
    return items_table.search(item.id == id)[0]

def get_all_items() -> list[Equipment]:
    return items_table.all()

def get_item_mod_by_idx(idx: int):
    return item_mods_table.get(doc_id=idx)

item_mod_count = item_mods_table.count(Query().id != "")
def get_item_mod_count() -> int:
    return item_mod_count

# - Cards ------
def to_card(doc: Document):
    mods_raw: list[Document] = doc["modifiers"]
    mods_real: list[CardModifierIndex] = list()

    for mod in mods_raw:
        mods_real.append(CardModifierIndex(mod["id"], mod["turns"], mod["amount"], mod["mode"]))

    return Card(doc["name"], doc["description"], doc["damage"], doc["target"], modsReal)

def get_card_by_name(name: str):
    card = Query()
    doc = card_table.search(card.name == name)[0]
    return to_card(doc)

def get_card_by_id(idx: int) -> Card:
    doc = card_table.get(doc_id=idx)
    return to_card(doc)

card_count = card_table.count(Query().id != "")
def get_card_count() -> int:
    if not card_count:
        return 0

    return card_count

def get_all_cards():
    cards_raw = card_table.all()
    cards_real: list[Card] = list()

    for card in cards_raw:
        cards_real.append(to_card(card))

    return cards_real

