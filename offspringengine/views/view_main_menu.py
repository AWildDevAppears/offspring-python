from typing import Callable
from toga import Box, Button
from toga.style.pack import Pack
from toga.widgets.base import Widget
from travertino.constants import COLUMN, RIGHT

from offspringengine.views.ui_component import UIComponent

from .constants import Views


def main_menu_view(
    switch_view: Callable[[Views], None],
    on_quit: Callable[[], None],
    parent: Widget,
):

    def func(self: UIComponent):

        def on_start_pressed(widget, **_):
            switch_view(Views.DUNGEON_REWARDS)

        def on_load_pressed(widget, **_):
            pass

        def on_quit_pressed(widget, **_):
            on_quit()

        start_button = Button("Start game", on_press=on_start_pressed)
        load_button = Button("Load game", on_press=on_load_pressed)
        quit_button = Button("Quit", on_press=on_quit_pressed)

        return Box(children=[
            start_button,
            load_button,
            quit_button,
        ],
                   style=Pack(padding=10, direction=COLUMN, alignment=RIGHT))

    return UIComponent(func, parent)
