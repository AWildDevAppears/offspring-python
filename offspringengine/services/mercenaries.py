from offspringengine.models.character import Character


def create_mercenaries():
    """Create a list of 3 new mercenaries to purchase"""

    merc1 = Character("aye")
    merc2 = Character("bee")
    merc3 = Character("cee")

    return [merc1, merc2, merc3]
