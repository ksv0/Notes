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

    def save(self):
        self.model.save_file()

    def first_action(self):
        pass

    def second_action(self):
        pass

    def third_action(self):
        pass

    def fourth_action(self):
        pass

    def fifth_action(self):
        pass

    def sixth_action(self):
        pass

    def seventh_action(self):
        pass

    def ninth_action(self):
        pass

    def load_first_preset(self):
        # общий экран
        # заполнить кнопки
        # вернуть список кнопок
        # print("""
        #             что делаем?
        #             1. вывести список заметок           | 4. добавить новую заметку     | 7.
        #             2. открыть заметку                  | 5.                            | 8.
        #             3. редактировать текущую заметку    | 6. сохранить                  | 9.
        #             """)
        pass

    def load_preset(self, screen: int = 1):
        match screen:
            case 1:
                self.load_first_preset()
            case 2:
                self.load_second_preset()


        pass

    def load_second_preset(self):
        # экран заметки
        # заполнить кнопки
        # вернуть список кнопок
        pass

    def print_descriptions(self, buttons: list[Button]):
        # получает список
        # собирает описание
        # отдает в вью описания кнопок
        pass

    def switch_action(self):
        pass
