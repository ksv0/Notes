from abc import abstractmethod, ABC
from app.ui.View import View


class ConsoleView(View):
    def __init__(self):
        pass

    def get(self):
        return str(input())

    def set(self, message):
        print(message)
