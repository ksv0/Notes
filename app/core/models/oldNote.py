import datetime

from app.core.models.Note import Note


class oldNote(Note):

    def __init__(self, note_id, title, notice):
        super().__init__(note_id, title, notice)

    def __str__(self):
        return f"{self.get_id}.\t{self.get_title}\n\t{self.get_create_date}\n\t{self.get_change_date}\n\t{self.get_notice}\n"
