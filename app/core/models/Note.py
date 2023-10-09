from datetime import datetime


class Note:
    def __init__(self, note_id, title, notice, create_date=datetime.now(), change_date=datetime.now()):
        self.__id: int = int(note_id)
        self.__title: str = title
        if isinstance(create_date, datetime):
            self.__create_date: datetime = create_date
            self.__change_date: datetime = change_date
        else:
            print("x is not a string")

        #if type(create_date) ==

        self.__notice: str = notice

    def __repr__(self):
        string = (
            f"{self.__id}. {self.__title}\ncreate date - {self.get_create_date_str()}\nchange date - {self.get_change_date_str()}\n{self.__notice}")
        return string

    def to_db(self):
        return (
            f"<{self.__id}><{self.__title}><{self.__notice}><{'{}.{}.{}  {}:{}'.format(self.__create_date.day, self.__create_date.month, self.__create_date.year, self.__create_date.hour, self.__create_date.minute)}><{'{}.{}.{}  {}:{}'.format(self.__change_date.day, self.__change_date.month, self.__change_date.year, self.__change_date.hour, self.__change_date.minute)}>")

    def get_create_date_str(self):
        return '{}.{}.{}  {}:{}'.format(self.__create_date.day, self.__create_date.month, self.__create_date.year,
                                        self.__create_date.hour, self.__create_date.minute)

    def get_change_date_str(self):
        return '{}.{}.{}  {}:{}'.format(self.__change_date.day, self.__change_date.month, self.__change_date.year,
                                        self.__change_date.hour, self.__change_date.minute)

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_create_date(self):
        return self.__create_date

    def get_change_date(self):
        return self.__change_date

    def get_notice(self):
        return self.__notice

    def set_id(self, id_: int):
        self.__id = id_

    def set_title(self, title: str):
        self.__title = title
        self.set_change_date()

    def set_change_date(self):
        self.__change_date = datetime.now()

    def set_notice(self, notice):
        self.__notice = notice
        self.set_change_date()
