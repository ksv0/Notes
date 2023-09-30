from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self, message):
        pass
