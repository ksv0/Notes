from abc import ABC, abstractmethod
from app.core.models.Note import Note


class Model(ABC):
    @abstractmethod
    def save_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def parser_from_zip(self):
        pass

    @abstractmethod
    def writer_to_zip(self):
        pass

    @abstractmethod
    def get_book(self) -> list[Note]:
        pass

    @abstractmethod
    def get_current_index(self):
        pass

    @abstractmethod
    def change_current_index(self, new_index: int):
        pass

    @abstractmethod
    def find(self, int_id):
        pass

    @abstractmethod
    def add_note(self, title, notice):
        pass

    @abstractmethod
    def set_title_in_current_note(self, new_title):
        pass

    @abstractmethod
    def set_notice_in_current_note(self, new_notice):
        pass

    @abstractmethod
    def delete_this_note(self):
        pass
