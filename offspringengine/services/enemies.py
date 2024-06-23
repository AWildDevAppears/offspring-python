##
# Copyright (c) AWildDevAppears
##

from offspringengine.models.character import Pawn
from offspringengine.services.database import get_enemy_by_id


class EnemyRef():
    def __init__(self, ref: str) -> None:
        descruct = ref.split(":")
        self.id = int(descruct[1])
        # self.modifiers = descruct[2]


def create_enemy_list_for(refs: list[str]) -> list[Pawn]:
    items: list[Pawn] = []

    for ref in refs:
        id = EnemyRef(ref).id
        items.append(get_enemy_by_id(id))

    return items
