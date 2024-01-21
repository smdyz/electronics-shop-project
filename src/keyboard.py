from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = "EN"
        self.__ch_l_flag = False

    def change_lang(self) -> None:
        if not self.__ch_l_flag:
            self.__ch_l_flag = True
            self.language = "RU"
            return None
        if self.__ch_l_flag:
            self.__ch_l_flag = False
            self.language = "EN"
            return None
