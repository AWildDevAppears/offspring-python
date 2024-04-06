from typing import Callable
from toga import Button, Widget, Box

from offspringengine.views.ui_component import UIComponent

from .constants import Views


def intro_view(switch_view: Callable[[Views], None], parent) -> Widget:

    def func():
        box = Box()

        def on_press(widget, **_):
            switch_view(Views.MAIN_MENU)

        button = Button("Button", on_press=on_press)
        box.add(button)
        return box

    return UIComponent(func, parent)
