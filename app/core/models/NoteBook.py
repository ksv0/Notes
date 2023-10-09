from app.core.models.Note import Note


class NoteBook:
    def __init__(self, note_book: list[Note]):
        self.__note_book: list[Note] = note_book

    def add_note(self, note: Note):
        self.__note_book.append(note)

    def get_note_book(self) -> list[Note]:
        return self.__note_book
