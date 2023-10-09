from app.core.Config import Config
from app.core.models.Button import Button
from app.core.mvp.model.Model import Model
from app.core.mvp.model.NoteModel import NoteModel
from app.core.mvp.presenter.Presenter import Presenter
from app.core.mvp.view.View import View


class NotePresenter(Presenter):

    def __init__(self, view: View):
        self.view: View = view
        self.config = Config()
        self.model: Model = NoteModel(self.config)
        self.screen: int = 1
        self.page: int = 0
        self.runnable: bool = True
        self.buttons: list[Button] = list()

    def get_flag(self) -> bool:
        return self.runnable

    def show_description(self):
        self.view.set("\n" * 100)
        match self.screen:
            case 1:
                self.show_full_list_desc()
            case 2:
                self.show_this_note()
        self.view.set_buttons_desc(self.buttons)

    def get_buttons(self) -> list[Button]:
        return self.buttons

    def save(self):
        self.model.save_file()

    def show_full_list_desc(self):
        self.view.set("Заметки\nid. Заголовок")
        where_from = self.page * self.config.get_how_much_to_view()
        for note in self.model.get_book()[where_from:where_from + self.config.get_how_much_to_view()]:
            self.view.set(f"{note.get_id()}. {note.get_title()}")
        if len(self.model.get_book()) != 0:
            self.view.set(
                f"Страница [{self.page + 1}/{len(self.model.get_book()) // self.config.get_how_much_to_view() + 1}]")

    def show_this_note(self):
        self.view.set(self.model.get_book()[self.model.get_current_index()].__repr__())

    def change_something_in_current_note(self):
        self.view.set("Что меняем")
        self.view.set("1. Заголовок    | 2. Заметку")
        match self.view.get(": "):
            case "1":
                self.model.set_title_in_current_note(self.view.get("Заголовок: "))
            case "2":
                self.model.set_notice_in_current_note(self.view.get("Заметка: "))

    def add_note(self):
        self.model.add_note(self.view.get("Заголовок: "), self.view.get("Заметка: "))

    def load_preset(self):
        match self.screen:
            case 1:
                self.load_first_preset()
            case 2:
                self.load_second_preset()

    def load_first_preset(self):
        self.screen = 1
        self.buttons = list()
        if len(self.model.get_book()) > self.config.get_how_much_to_view():
            if self.page > 0:
                self.buttons.append(Button("влево                           ", self.page_left))
            if (self.page + 1) * self.config.get_how_much_to_view() < len(self.model.get_book()):
                self.buttons.append(Button("вправо                          ", self.page_right))
        if len(self.model.get_book()) > 0:
            self.buttons.append(Button("открыть заметку                 ", self.open_note))
        self.buttons.append(Button("добавить новую заметку          ", self.add_note))
        self.buttons.append(Button("сохранить                       ", self.save))
        self.buttons.append(Button("выход                           ", self.escape))

    def load_second_preset(self):
        self.screen = 2
        self.buttons = list()
        if len(self.model.get_book()) != 0:
            if self.model.get_current_index() > 0:
                self.buttons.append(Button("влево                           ", self.note_left))
            if self.model.get_current_index() < len(self.model.get_book()) - 1:
                self.buttons.append(Button("вправо                          ", self.note_right))
        self.buttons.append(Button("вывести список заметок          ", self.to_full_list))
        self.buttons.append(Button("редактировать текущую заметку   ", self.change_something_in_current_note))
        self.buttons.append(Button("удалить заметку                 ", self.delete_this_note))
        self.buttons.append(Button("добавить новую заметку          ", self.add_note))
        self.buttons.append(Button("сохранить                       ", self.save))
        self.buttons.append(Button("выход                           ", self.escape))

    def to_full_list(self):
        self.screen = 1

    def note_left(self):
        self.model.change_current_index(self.model.get_current_index() - 1)

    def note_right(self):
        self.model.change_current_index(self.model.get_current_index() + 1)

    def page_left(self):
        self.page -= 1

    def page_right(self):
        self.page += 1

    def load_third_preset(self):
        pass

    def open_note(self):
        try:
            int_id: int = int(self.view.get("id: "))
            self.model.change_current_index(self.model.find(int_id))
            self.screen = 2
        except Exception as e:
            self.view.set(e.__str__())

    def escape(self):
        self.runnable = False

    def delete_this_note(self):
        self.model.delete_this_note()
