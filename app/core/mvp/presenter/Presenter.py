from abc import ABC, abstractmethod

from app.core.models.Button import Button


class Presenter(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_buttons(self) -> list[Button]:
        pass

    @abstractmethod
    def show_full_list_desc(self):
        pass

    @abstractmethod
    def show_this_note(self):
        pass

    @abstractmethod
    def change_something_in_current_note(self):
        pass

    @abstractmethod
    def add_note(self):
        pass

    @abstractmethod
    def load_preset(self):
        pass

    @abstractmethod
    def load_first_preset(self):
        pass

    @abstractmethod
    def load_second_preset(self):
        pass


    @abstractmethod
    def show_description(self):
        pass

    @abstractmethod
    def get_flag(self):
        pass
