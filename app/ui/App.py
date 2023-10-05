from app.core.models.Button import Button
from app.core.mvp.presenter.NotePresenter import NotePresenter
from app.core.mvp.presenter.Presenter import Presenter
from app.core.mvp.view.ConsoleView import ConsoleView
from app.core.mvp.view.View import View


class App:
    def __init__(self):
        self.view: View = ConsoleView()
        self.presenter: Presenter = NotePresenter(self.view)
        self.screen: int = 1

    def run(self):
        flag: bool = True
        buttons: list[Button]

        while flag:

            self.view.set(self.presenter.load_preset(self.screen))
            match self.view.get():# вынести в функцию
                case 1:

                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    self.presenter.save()
            pass
        pass
