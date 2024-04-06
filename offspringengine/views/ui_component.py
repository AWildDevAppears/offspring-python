from toga.widgets.base import Widget


class UIComponent():

    def __init__(self, rerender, parent: Widget) -> None:
        self.current = None
        self.parent = parent
        self.rerender = rerender
        self.change_hook = None

    def on_change(self):
        self.parent.remove(self.current)
        self.current = self.rerender(self)
        self.parent.add(self.current)

        if self.change_hook is not None:
            self.change_hook(self.current)

    def on_mount(self, change_hook):
        self.current = self.rerender(self)
        self.change_hook = change_hook

        change_hook(self.current)
