import csv
from zipfile import ZipFile

from app.core.Config import Config
from app.core.models.Note import Note
from app.core.models.NoteBook import NoteBook
from app.core.mvp.model.Model import Model


class NoteModel(Model):
    def __init__(self, config: Config):
        self.config: Config = config
        self.book: NoteBook = NoteBook(self.read_file())
        self.current_index: int = 0

    def get_current_index(self):
        return self.current_index

    def change_current_index(self, new_index: int):
        self.current_index = new_index

    def get_book(self):
        return self.book

    def read_file(self) -> list[Note]:
        notes: list[Note] = list()
        raw_notes: list[list[str]]

        if self.config.get_path_to_resources().endswith(".zip"):
            raw_notes = self.parser_from_zip()
        else:
            return notes

        if raw_notes.__sizeof__():
            return notes
        for row in raw_notes:
            notes.append(Note(row[0], row[1], row[2], row[3], row[4]))
        return notes

    def parser_from_zip(self) -> list[list[str]]:
        lines: list[list[str]] = list()
        with ZipFile(self.config.path_to_current_notebook, "r") as zip_file:
            i: int = 0
            while i < len(zip_file.namelist()):
                with zip_file.open(zip_file.namelist()[i], "r") as note:
                    lines.append(note.readlines().__str__()[1:-2].split("><"))  # проверить
                i += 1
        return lines

    # говно не сработает
    def parser_csv(self) -> list[list[str]]:
        lines: list[list[str]] = list()
        with open(self.config.path_to_current_notebook, "r") as fr:
            if fr.__sizeof__() == 0:
                return lines
            reader = csv.reader(fr)
            for line in reader:
                lines.append(line)
        return lines

    def save_file(self):
        if self.config.get_path_to_resources().endswith(".zip"):
            self.writer_to_zip()

    def writer_to_zip(self):
        with ZipFile(self.config.path_to_current_notebook, "w") as zip_file:
            i: int = 0
            while i < len(self.book.get_note_book()):
                with zip_file.open(self.book.get_note_book()[i].get_title(), "w") as note:
                    note.write(self.book.get_note_book()[i].to_db())
                i += 1

    def writer_csv(self):
        with open(self.config.path_to_current_notebook, "w", newline="") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.book.get_note_book())
