from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def save_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def parser_csv(self): # to_delete
        pass

    @abstractmethod
    def writer_csv(self): # to_delete
        pass

    @abstractmethod
    def parser_from_zip(self):
        pass

    @abstractmethod
    def writer_to_zip(self):
        pass

    pass

    @abstractmethod
    def get_book(self):
        pass

    @abstractmethod
    def get_current_index(self):
        pass

    @abstractmethod
    def change_current_index(self, new_index: int):
        pass
