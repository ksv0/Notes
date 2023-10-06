from typing import Callable

from app.core.Config import Config
from app.core.models.Button import Button
from app.core.mvp.model.Model import Model
from app.core.mvp.model.NoteModel import NoteModel
from app.core.mvp.presenter.Presenter import Presenter
from app.core.mvp.view.ConsoleView import ConsoleView
from app.core.mvp.view.View import View


class NotePresenter(Presenter):

    def __init__(self, view: View):
        self.view: View = view
        self.config = Config()
        self.model: Model = NoteModel(self.config)
        self.screen: int = 1
        self.buttons: list[Button] = list()

    def save(self):  # сохранить все, конфиг, модель и пока все # todo
        self.model.save_file()

    def show_full_list_desc(self):
        for note in self.model.get_book().get_note_book():
            self.view.set(note.get_title())

    def show_this_note(self):
        self.view.set(self.model.get_book().get_note_book()[self.model.get_current_index()].get_id + ". " +
                      self.model.get_book().get_note_book()[self.model.get_current_index()].get_title())
        self.view.set(self.model.get_book().get_note_book()[self.model.get_current_index()].get_create_date_str())
        self.view.set(self.model.get_book().get_note_book()[self.model.get_current_index()].get_change_date_str())
        self.view.set(self.model.get_book().get_note_book()[self.model.get_current_index()].get_notice())

    def change_something_in_current_note(self):  # я еще хз че получать, че отправлять
        pass

    def add_note(
            self):  # тут должен быть переход на третий экран, создание заметки, переход на предыдущий экран UPD. все переходы в свитч
        self.view.get()

    def fifth_action(self):
        pass

    def sixth_action(self):
        pass

    def seventh_action(self):
        pass

    def ninth_action(self):
        pass

    def load_preset(self):  # эту хуйню вызываем из свича
        # первый экран - полный список заметок(мб сделать в 2 колонки, либо расширяющимся как в )
        # второй экран - экран заметки
        # третий экран - заполнение заметки
        match self.screen:
            case 1:
                self.load_first_preset()
            case 2:
                self.load_second_preset()
            case 3:
                self.load_third_preset()

    def load_first_preset(self):  # узнать как добавить типа джавадок но пайтон
        self.screen = 1
        self.buttons = list()
        self.buttons.append(Button("открыть заметку"))
        self.buttons.append(Button("добавить новую заметку"))
        self.buttons.append(Button("сохранить"))
        if len(self.model.get_book()) > self.config.get_how_much_to_view():
            self.buttons.append(Button("влево"))
            self.buttons.append(Button("вправо"))
        self.buttons.append(Button("выход"))

        # общий экран
        # заполнить кнопки #

        # print(""" # как напоминание
        #             что делаем?
        #             1. вывести список заметок           | 4. добавить новую заметку     | 7.вправо
        #             2. открыть заметку                  | 5. удалить заметку            | 8.влево
        #             3. редактировать текущую заметку    | 6. сохранить                  | 9.выход         10 корзина
        #             """)
        pass

    def load_second_preset(self):
        self.screen = 2
        self.buttons = list()

        # экран заметки
        # заполнить кнопки
        # вернуть список кнопок
        pass

    def print_descriptions(self):  # !!!!!!!!!!!!!!!!!!!!!!
        # собирает описание
        # отдает в вью описания кнопок
        pass

    def switch_action(self):  # перенести в презентер маркер экрана
        # вызывает шоу текущего экрана
        # запрашивает у пользователя действие
        # жмет соответствующую кнопку
        pass

    def load_third_preset(self):
        pass
