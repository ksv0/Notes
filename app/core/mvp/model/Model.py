from app.core.models.Note import Note
from app.core.models.NoteBook import NoteBook
import csv


class Model:
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.book: NoteBook = NoteBook(self.read_file())
        self.current_index: int = 0

    def read_file(self) -> list[Note]:
        notes: list[Note] = list()
        if self.file_name.endswith(".csv"):
            raw_notes: list[list[str]] = self.parser_csv()

        if raw_notes.__sizeof__():
            return notes
        for row in raw_notes:
            notes.append(Note(row[0], row[1], row[2], row[3], row[4]))
        return notes

    def parser_csv(self) -> list[list[str]]:
        lines: list[list[str]] = list()
        with open(self.file_name, "r") as fr:
            if fr.__sizeof__() == 0:
                return lines
            reader = csv.reader(fr)
            for line in reader:
                lines.append(line)
        return lines

    def save_file(self):
        if self.file_name.endswith(".csv"):
            self.writer_csv()

    def writer_csv(self):
        with open(self.file_name, "w", newline="") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.book.get_note_book())

