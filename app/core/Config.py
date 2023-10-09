import os


class Config:
    path_to_current_notebook: str = os.path.abspath("../resources/note.zip").replace("\\", "/")
    path_to_config: str = "app/core/config.ini"
    how_much_to_view: int = 5

    def __init__(self):
        self.read_config()

    def set_how_much_to_view(self, how_much_to_view: int):
        self.how_much_to_view = how_much_to_view

    def get_how_much_to_view(self) -> int:
        return self.how_much_to_view

    def set_path_to_resources(self, new_path: str):
        self.path_to_current_notebook = new_path

    def set_path_to_config(self, new_path):
        self.path_to_config = new_path

    def get_path_to_book(self) -> str:
        return self.path_to_current_notebook

    def get_path_to_config(self) -> str:
        return self.path_to_config

    def read_config(self):  # todo лень
        pass

    def save_config(self):  # todo не буду делать
        pass
