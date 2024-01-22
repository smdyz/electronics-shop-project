from src.item import Item


class LanguageMixin:
    __ch_l_flag = False

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self) -> None:
        if not self.__ch_l_flag:
            self.__ch_l_flag = True
            self.__language = "RU"
            return None
        if self.__ch_l_flag:
            self.__ch_l_flag = False
            self.__language = "EN"
            return None


class Keyboard(LanguageMixin, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__ch_l_flag = False

