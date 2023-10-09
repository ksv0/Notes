from abc import ABC, abstractmethod

from app.core.models.Button import Button


class View(ABC):
    @abstractmethod
    def get(self, message=""):
        pass

    @abstractmethod
    def set(self, message):
        pass

    @abstractmethod
    def set_buttons_desc(self, buttons: list[Button]):
        pass
