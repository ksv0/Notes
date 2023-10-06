from abc import ABC, abstractmethod

# разделить интерфейсы
class Presenter(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def show_full_list_desc(self):
        pass

    @abstractmethod
    def show_this_note(self):
        pass

    @abstractmethod
    def change_something_in_current_note(self):
        pass

    @abstractmethod
    def add_note(self):
        pass

    @abstractmethod
    def fifth_action(self):
        pass

    @abstractmethod
    def sixth_action(self):
        pass

    @abstractmethod
    def seventh_action(self):
        pass

    @abstractmethod
    def ninth_action(self):
        pass

    @abstractmethod
    def switch_action(self):
        pass

    @abstractmethod
    def load_preset(self, screen: int = 1):
        pass

    @abstractmethod
    def load_first_preset(self):
        # общий экран
        # заполнить кнопки
        # вернуть список кнопок
        # print("""
        #             что делаем?
        #             1. вывести список заметок           | 4. добавить новую заметку     | 7.
        #             2. открыть заметку                  | 5.                            | 8.
        #             3. редактировать текущую заметку    | 6. сохранить                  | 9.
        pass

    @abstractmethod
    def load_second_preset(self):
        # экран заметки
        # заполнить кнопки
        # вернуть список кнопок
        pass

    @abstractmethod
    def load_third_preset(self):
        pass
