from app.core.Config import Config
from app.core.models.Button import Button
from app.core.mvp.view.View import View


class ConsoleView(View):
    def __init__(self):
        pass

    def set_buttons_desc(self, buttons: list[Button]):
        string = ""
        for i in range(0, len(buttons)):
            if i % 2 == 0:
                self.set(string)
                string = ""
            string += f"{i + 1}. {buttons[i].get_desc()}| "
        self.set(string)

    def get(self, message=""):
        return str(input(message))

    def set(self, message):
        print(message)
