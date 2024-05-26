

from random import randint
from offspringengine.models.card import Card
from offspringengine.services.database import get_card_by_id, get_card_count


def get_random_card_pack(size: int) -> list[Card]:
    min = 1
    max: int = get_card_count()

    indexes: list[int] = list()
    items: list[Card] = list()

    for i in range(size):
        idx: int = randint(min, max)


        while idx in indexes:
            idx = randint(min, max)

        indexes.append(idx)
        items.append(get_card_by_id(idx))

    return items

