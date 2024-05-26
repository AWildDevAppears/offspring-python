from enum import Enum


class CardTarget(Enum):
    SELF = "self"
    ENEMY = "enemy"
    ENEMY_ALL = "enemy_all"
    ALL = "all"
    ARENA = "arena"
    SPELL = "spell"


class CardModifierType(Enum):
    APPLY = "apply"
    NEGATE = "negate"


class CardModifierIndex():
    def __init__(self, id: str, turns: int, amount: int, mode: CardModifierType) -> None:
        self.id = id
        self.turns = turns
        self.amount = amount
        self.mode = mode


class Card:
    def __init__(self, name: str, descrition: str, damage: int, target: CardTarget, modifiers: list[str]):
        self.name: str = name
        self.descrition: str = descrition
        self.damage: int = damage
        self.target: CardTarget = target
        self.modifiers = modifiers


