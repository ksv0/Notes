from datetime import datetime


class Note:
    def __init__(self, note_id, title, create_date, change_date, notice):
        self.__id: int = int(note_id)
        self.__title: str = title
        self.__create_date: datetime = datetime.strptime(create_date, "%d.%m.%Y %H:%M")
        self.__change_date: datetime = datetime.strptime(change_date, "%d.%m.%Y %H:%M")
        self.__notice: str = notice

    def __str__(self):
        pass

    def to_db(self):
        return f"<{self.__id}><{self.__title}><{'{}.{}.{}  {}:{}'.format(self.__create_date.day, self.__create_date.month, self.__create_date.year, self.__create_date.hour, self.__create_date.minute)}><{'{}.{}.{}  {}:{}'.format(self.__change_date.day, self.__change_date.month, self.__change_date.year, self.__change_date.hour, self.__change_date.minute)}><{self.__notice}>"

    def get_create_date_str(self):
        return '{}.{}.{}  {}:{}'.format(self.__create_date.day, self.__create_date.month, self.__create_date.year, self.__create_date.hour, self.__create_date.minute)

    def get_change_date_str(self):
        return '{}.{}.{}  {}:{}'.format(self.__change_date.day, self.__change_date.month, self.__change_date.year, self.__change_date.hour, self.__change_date.minute)

    def to_csv(self):
        return f"{self.__id},{self.__title},{self.get_create_date_str()},{self.get_change_date_str()},{self.__notice}"

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

    def set_id(self, id: int):
        self.__id = id

    def set_title(self, title: str):
        self.__title = title

    def set_change_date(self, new_change_date):
        self.__change_date = new_change_date

    def set_notice(self, notice):
        self.__notice = notice
