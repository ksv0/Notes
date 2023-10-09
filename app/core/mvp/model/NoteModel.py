import csv
from datetime import datetime
from zipfile import ZipFile
import os

from setuptools import glob

from app.core.Config import Config
from app.core.models.Note import Note
from app.core.models.NoteBook import NoteBook
from app.core.mvp.model.Model import Model


class NoteModel(Model):
    def __init__(self, config: Config):
        self.config: Config = config
        self.book: NoteBook = NoteBook(self.read_file())
        self.current_index: int = 0

    def delete_this_note(self):
        self.book.get_note_book().pop(self.current_index)
        if self.current_index == len(self.book.get_note_book()):
            self.current_index -= 1
        if self.current_index == -1:
            self.current_index = 0

    def set_title_in_current_note(self, new_title):
        self.book.get_note_book()[self.current_index].set_title(new_title)

    def set_notice_in_current_note(self, new_notice):
        self.book.get_note_book()[self.current_index].set_notice(new_notice)
        pass

    def add_note(self, title, notice):
        self.book.add_note(Note(len(self.book.get_note_book()) + 1, title, notice))

    def find(self, int_id: int) -> int:
        for item in self.book.get_note_book():
            if item.get_id() == int_id:
                return self.book.get_note_book().index(item)
        raise Exception("id не найден")

    def change_current_index(self, new_index: int):
        self.current_index = new_index

    def get_current_index(self) -> int:
        return self.current_index

    def get_book(self) -> list[Note]:
        return self.book.get_note_book()

    def read_file(self) -> list[Note]:
        notes: list[Note] = list()
        raw_notes: list[list[str]]
        raw_notes = self.parser_from_zip()
        for row in raw_notes:
            notes.append(Note(row[0], row[1], row[2], datetime.strptime(row[3], "%d.%m.%Y %H:%M"),
                              datetime.strptime(row[4], "%d.%m.%Y %H:%M")))
        return notes

    def parser_from_zip(self) -> list[list[str]]:
        lines: list[list[str]] = list()
        try:
            path = "tmp/"
            with ZipFile(self.config.path_to_current_notebook, "r") as zip_file:
                zip_file.extractall(path, pwd="python_soset_zhopy".encode("UTF-8"))
                zip_file.close()
            rez = sorted(os.listdir(path))
            for n, item in enumerate(rez):
                with open(os.path.join(path, item), 'r', encoding="utf-8") as f:
                    string = f.readline().__str__()[1:-1].split("><")
                    lines.append(string)
                os.remove(os.path.join(path, item))
            os.rmdir(path)
        except FileNotFoundError as e:
            print(e)
        return lines

    def save_file(self):
        if self.config.get_path_to_book().endswith(".zip"):
            self.writer_to_zip()

    def writer_to_zip(self):
        with ZipFile(self.config.get_path_to_book(), "w"):
            pass
        with ZipFile(self.config.get_path_to_book(), "a") as zip_:
            for item in self.book.get_note_book():
                zip_.writestr(item.get_id().__str__() + " " + item.get_title() + ".txt", item.to_db())
            zip_.setpassword("python_soset_zhopy".encode("UTF-8"))
