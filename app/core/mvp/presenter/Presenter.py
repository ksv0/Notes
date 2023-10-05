from abc import ABC, abstractmethod


class Presenter(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def first_action(self):
        pass

    @abstractmethod
    def second_action(self):
        pass

    @abstractmethod
    def third_action(self):
        pass

    @abstractmethod
    def fourth_action(self):
        pass

    @abstractmethod
    def fifth_action(self):
        pass

    @abstractmethod
    def sixth_action(self):
        pass

    @abstractmethod
    def seventh_action(self):
        pass

    @abstractmethod
    def ninth_action(self):
        pass

    @abstractmethod
    def load_first_preset(self):
        pass

    @abstractmethod
    def load_preset(self, screen: int = 1):
        pass
