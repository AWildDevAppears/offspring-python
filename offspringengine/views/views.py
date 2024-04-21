from typing import cast
import toga
from toga.app import App
from toga.widgets.base import Widget
from toga.widgets.box import Box

from offspringengine.views.ui_component import UIComponent

from . import view_intro, view_main_menu, view_dungeon_rewards, constants


class OffspringApp(App):

    def startup(self) -> None:
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = Box()

        # List of views
        self.views: dict[constants.Views, UIComponent] = {
            constants.Views.INTRO:
                view_intro.intro_view(self.switch_view,
                                      self.main_window.content),
            constants.Views.MAIN_MENU:
                view_main_menu.main_menu_view(self.switch_view,
                                              self.quit_action,
                                              self.main_window.content),
            constants.Views.DUNGEON_REWARDS:
                view_dungeon_rewards.rewards_screen(self.switch_view,
                                                    self.main_window.content),
        #     constants.Views.MERCENARY_SELECT:
        #         view_character_choose.merc_select(self.switch_view)
        }

        view = self.views[constants.Views.MAIN_MENU]
        view.on_mount(self.on_change)

        self.current_view = view.current
        self.main_window.content.add(self.current_view)

        self.main_window.show()

    def switch_view(self, key: constants.Views):
        print(key, self.views.keys())

        if self.main_window.content is None:
            return

        if key not in self.views.keys():
            return

        self.main_window.content.remove(self.current_view)

        self.current_view = None

        view = self.views[key]
        view.on_mount(self.on_change)

        self.current_view = view.current
        self.main_window.content.add(self.current_view)

    def quit_action(self):
        if self.app is not None:
            self.app.exit()

    def on_change(self, replaced_view: Widget):
        self.current_view = replaced_view


def init():
    return OffspringApp("Offspring", "uk.co.awilddevappears.offspring")
