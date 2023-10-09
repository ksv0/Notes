from app.core.models.Button import Button
from app.core.mvp.presenter.NotePresenter import NotePresenter
from app.core.mvp.presenter.Presenter import Presenter
from app.core.mvp.view.ConsoleView import ConsoleView
from app.core.mvp.view.View import View


class App:
    def __init__(self):
        self.view: View = ConsoleView()
        self.presenter: Presenter = NotePresenter(self.view)

    def run(self):
        while self.presenter.get_flag():
            self.presenter.load_preset()
            self.presenter.show_description()
            try:
                i: int = int(self.view.get())
                self.presenter.get_buttons()[i-1].press()
            except Exception as e:
                self.view.set("Нет такой функции!")

        pass
