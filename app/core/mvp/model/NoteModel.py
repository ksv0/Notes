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

    def read_file(self) -> list[Note]:
        notes: list[Note] = list()
        raw_notes: list[list[str]]

        if self.config.get_path_to_resources().endswith(".zip"):
            raw_notes = self.parser_from_zip()
        else:
            return notes
        # if self.config.get_path_to_resources().endswith(".csv"):
        #     raw_notes = self.parser_csv()
        # else:
        #    self.config.set_path_to_resources(self.config.get_path_to_resources()+".csv")

        if raw_notes.__sizeof__():
            return notes
        for row in raw_notes:
            notes.append(Note(row[0], row[1], row[2], row[3], row[4]))
        return notes

    def parser_from_zip(self):
        lines: list[list[str]] = list()
        with ZipFile(self.config.path_to_current_notebook, "r") as zip_file:
            i: int = 0
            while i < len(zip_file.namelist()):
                with zip_file.open(zip_file.namelist()[i], "r") as note:
                    lines.append(note.readlines().__str__()[1:-2].split("><"))# проверить
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
        # if self.config.path_to_current_note.endswith(".csv"):
        #     self.writer_csv()

    def writer_to_zip(self):
        with ZipFile(self.config.path_to_current_notebook, "w"):
            pass # here тут где ult
        pass

    def writer_csv(self):
        with open(self.config.path_to_current_notebook, "w", newline="") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.book.get_note_book())
