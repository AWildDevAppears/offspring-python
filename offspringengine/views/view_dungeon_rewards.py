from typing import Callable
from toga import Box
import toga
from toga.style.pack import Pack
from toga.widgets.button import Button
from toga.widgets.label import Label
from travertino.constants import COLUMN, LEFT

from offspringengine.models.equipment import (
    EquipmentType,
)
from offspringengine.services.equipment import get_random_equippable
from offspringengine.views.ui_component import UIComponent

from .constants import Views


class EquipmentRoller(object):
    def __init__(self) -> None:
        super().__init__()
        self.item: EquipmentType | None = None

    def roll(self):
        self.item = get_random_equippable()


roller = EquipmentRoller()


def rewards_screen(
    switch_view: Callable[[Views], None], parent: toga.Widget
) -> UIComponent:
    def func(self: UIComponent):
        roller.roll()

        def on_reroll_pressed(widget: toga.Widget, **_):
            roller.roll()
            self.on_change()

        def on_back_pressed(widget: toga.Widget, **_):
            switch_view(Views.MAIN_MENU)

        if roller.item is None:
            return


        item_name = Label(f"Name: {roller.item.full_name()}")
        item_defence = Label(f"Defence: {roller.item.defence}")
        reroll_button = Button("Re-roll", on_press=on_reroll_pressed)
        back_button = Button("Go back", on_press=on_back_pressed)

        widgets = [
            item_name,
            item_defence,
        ]

        if roller.item.mods is not None:
            for mod in roller.item.mods:
                widgets.append(Label(f"Mod: {mod.name}"))

        widgets.append(reroll_button)
        widgets.append(back_button)

        return Box(
            children=widgets,
            style=Pack(direction=COLUMN, alignment=LEFT, padding=10),
        )

    return UIComponent(func, parent)
