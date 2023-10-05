from typing import Callable


class Button:
    def __init__(self, desc: str, func: Callable = None):
        self.desc: str = desc
        self.func_list: list[Callable] = list()
        if func is not None:
            self.func_list.append(func)

    def get_desc(self):
        return self.desc

    def press(self):
        for f in self.func_list:
            f()

    def add_func(self, func: Callable):
        self.func_list.append(func)
