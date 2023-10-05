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
